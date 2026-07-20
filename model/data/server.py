import socket
import threading

from protocol import send_message, receive_messages
from room_service import RoomService
from chat_service import ChatService


HOST = "127.0.0.1"
PORT = 5000


class ChatServer:
    def __init__(self):
        # 접속한 클라이언트 소켓 목록
        self.clients = []

        # 사용자 ID와 소켓을 연결해서 저장
        self.login_clients = {}

        # 방 관련 기능 처리 객체
        self.room_service = RoomService()

        # 채팅 관련 기능 처리 객체
        self.chat_service = ChatService()

    # 서버 시작 함수
    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((HOST, PORT))

        server_socket.listen()

        print("[서버 시작]")
        print(f"[주소] {HOST}:{PORT}")
        print("[클라이언트 접속 대기 중...]")

        while True:
            client_socket, client_address = server_socket.accept()

            print(f"[클라이언트 접속] {client_address}")

            self.clients.append(client_socket)

            thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, client_address)
            )

            thread.daemon = True
            thread.start()

    # 클라이언트 한 명을 처리하는 함수
    def handle_client(self, client_socket, client_address):
        buffer = ""

        while True:
            buffer, messages, is_connected = receive_messages(client_socket, buffer)

            if not is_connected:
                print(f"[연결 종료] {client_address}")
                break

            for message in messages:
                print("[받은 메시지]")
                print(message)

                self.handle_message(client_socket, message)

        if client_socket in self.clients:
            self.clients.remove(client_socket)

        remove_id = None

        for id, sock in self.login_clients.items():
            if sock == client_socket:
                remove_id = id
                break

        if remove_id is not None:
            del self.login_clients[remove_id]
            print(f"[사용자 연결 해제] {remove_id}")

        client_socket.close()

    # 메시지 type에 따라 기능 분리
    def handle_message(self, client_socket, message):
        message_type = message.get("type")

        if message_type == "connect_user":
            self.handle_connect_user(client_socket, message)

        elif message_type == "room":
            self.handle_make_room(client_socket, message)

        elif message_type == "room_list":
            self.handle_room_list(client_socket, message)

        elif message_type == "join_room":
            self.handle_join_room(client_socket, message)

        elif message_type == "out_room":
            self.handle_out_room(client_socket, message)

        elif message_type == "invite_room":
            self.handle_invite_room(client_socket, message)

        elif message_type == "message":
            self.handle_chat_message(client_socket, message)

        elif message_type == "chat_list":
            self.handle_chat_list(client_socket, message)

        elif message_type == "ping":
            send_message(client_socket, {
                "type": "system",
                "success": True,
                "message": "서버 연결 성공"
            })

        else:
            send_message(client_socket, {
                "type": "error",
                "success": False,
                "message": f"지원하지 않는 메시지 타입입니다: {message_type}"
            })

    # 사용자 연결 등록 처리
    def handle_connect_user(self, client_socket, message):
        id = message.get("id")

        if id is None or id.strip() == "":
            send_message(client_socket, {
                "type": "connect_user",
                "success": False,
                "id": id,
                "message": "사용자 연결 등록 실패: 사용자 ID가 없습니다."
            })
            return

        self.login_clients[id] = client_socket

        print(f"[사용자 연결 등록] {id}")

        send_message(client_socket, {
            "type": "connect_user",
            "success": True,
            "id": id,
            "message": "사용자 연결 등록 성공"
        })

    # 같은 방 멤버들에게 메시지 전달
    def send_message_to_room_members(self, members, message):
        send_data = message.copy()

        if "member" in send_data:
            del send_data["member"]

        for id in members:
            if id in self.login_clients:
                client_socket = self.login_clients[id]

                try:
                    send_message(client_socket, send_data)

                except Exception:
                    print(f"[오류] {id}에게 메시지 전송 실패")

    # 같은 방 멤버들에게 알림 전송
    def send_notice_to_room_members(self, members, notice):
        send_data = notice.copy()

        if "member" in send_data:
            del send_data["member"]

        for id in members:
            if id in self.login_clients:
                client_socket = self.login_clients[id]

                try:
                    send_message(client_socket, send_data)

                except Exception:
                    print(f"[오류] {id}에게 알림 전송 실패")

    # 채팅방 생성 처리
    def handle_make_room(self, client_socket, message):
        ids = message.get("id")
        nicknames = message.get("nickname")

        result = self.room_service.make_room(
            ids,
            nicknames
        )

        if not result.get("success"):
            send_message(client_socket, result)
            return

        members = result.get("member", [])

        self.send_notice_to_room_members(
            members,
            result
        )

    # 채팅방 목록 조회 처리
    def handle_room_list(self, client_socket, message):
        id = message.get("id")

        result = self.room_service.get_room_list(id)

        send_message(client_socket, result)

    # 채팅방 입장 처리
    def handle_join_room(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")

        result = self.room_service.join_room(
            room_id,
            id
        )

        if not result.get("success"):
            send_message(client_socket, result)
            return

        chat_result = self.chat_service.get_chat_list(
            room_id,
            id
        )

        result["chat"] = chat_result.get("chat", [])

        send_message(client_socket, result)

    # 채팅방 나가기 처리
    def handle_out_room(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")

        result = self.room_service.out_room(
            room_id,
            id
        )

        if not result.get("success"):
            send_message(client_socket, result)
            return

        send_message(client_socket, result)

        members = result.get("member", [])

        notice = {
            "type": "out_room_notice",
            "success": True,
            "room_id": result.get("room_id"),
            "id": result.get("id"),
            "room": result.get("room"),
            "message": f"{result.get('id')}님이 방을 나갔습니다."
        }

        self.send_notice_to_room_members(
            members,
            notice
        )

    # 채팅방 친구 초대 처리
    def handle_invite_room(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")
        nickname = message.get("nickname")

        result = self.room_service.invite_room(
            room_id,
            id,
            nickname
        )

        if not result.get("success"):
            send_message(client_socket, result)
            return

        members = result.get("member", [])

        self.send_notice_to_room_members(
            members,
            result
        )

    # 채팅 메시지 전송 처리
    def handle_chat_message(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")
        nickname = message.get("nickname")
        content = message.get("content")

        result = self.chat_service.send_chat(
            room_id,
            id,
            nickname,
            content
        )

        if not result.get("success"):
            send_message(client_socket, result)
            return

        members = result.get("member", [])

        self.send_message_to_room_members(
            members,
            result
        )

    # 채팅 기록 조회 처리
    def handle_chat_list(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")

        result = self.chat_service.get_chat_list(
            room_id,
            id
        )

        send_message(client_socket, result)


if __name__ == "__main__":
    server = ChatServer()
    server.start()