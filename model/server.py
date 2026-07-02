import socket
import threading

from protocol import send_message, receive_messages
from chat_room import RoomService
from chat_service import ChatService
from member_repo import MemberRepo

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
        self.member_repo = MemberRepo()

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
            self.broadcast_user_list()
        client_socket.close()

    # 메시지 type에 따라 기능 분리
    def handle_message(self, client_socket, message):
        message_type = message.get("type")

        if message_type == "connect_user":
            self.handle_connect_user(client_socket, message)
        elif message_type == "user_list":
            self.handle_user_list(client_socket, message)
        elif message_type == "member_list":
            self.handle_member_list(client_socket, message)
        elif message_type == "room_member_list":
            self.handle_room_member_list(client_socket, message)
        elif message_type == "invite_member_list":
            self.handle_invite_member_list(client_socket, message)
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
        self.broadcast_user_list()

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

    # 접속자 목록 조회 처리
    def handle_user_list(self, client_socket, message):
        users = list(self.login_clients.keys())

        send_message(client_socket, {
            "type": "user_list",
            "success": True,
            "users": users,
            "message": "접속자 목록 조회 성공"
        })

    # 전체 접속자에게 접속자 목록 전송
    def broadcast_user_list(self):
        users = list(self.login_clients.keys())

        message = {
            "type": "user_list",
            "success": True,
            "users": users,
            "message": "접속자 목록 갱신"
        }
        for id, client_socket in self.login_clients.items():
            try:
                send_message(client_socket, message)
            except Exception:
                print(f"[오류] {id}에게 접속자 목록 전송 실패")

    # 전체 회원 목록 + 온라인 상태 조회 처리
    def handle_member_list(self, client_socket, message):
        members = self.member_repo.find_all_members()

        result = []

        for member in members:
            member_id = member.get("id", "")
            nickname = member.get("nickname", "")

            if member_id in self.login_clients:
                status = "online"
            else:
                status = "offline"

            result.append({
                "id": member_id,
                "nickname": nickname,
                "status": status
            })

        send_message(client_socket, {
            "type": "member_list",
            "success": True,
            "member": result,
            "message": "전체 회원 목록 조회 성공"
        })

    # 초대 가능한 회원 목록 조회 처리
    def handle_invite_member_list(self, client_socket, message):
        room_id = message.get("room_id")
        id = message.get("id")

        # room_id 숫자 변환
        try:
            room_id = int(room_id)
        except (TypeError, ValueError):
            send_message(client_socket, {
                "type": "invite_member_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "member": [],
                "message": "초대 가능한 회원 목록 조회 실패: 방 번호가 올바르지 않습니다."
            })
            return
        # 사용자 ID 검사
        if id is None or id.strip() == "":
            send_message(client_socket, {
                "type": "invite_member_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "member": [],
                "message": "초대 가능한 회원 목록 조회 실패: 사용자 ID가 없습니다."
            })
            return

        # 채팅방 조회
        room = self.room_service.room_repo.find_room_by_id(room_id)

        if room is None:
            send_message(client_socket, {
                "type": "invite_member_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "member": [],
                "message": "초대 가능한 회원 목록 조회 실패: 존재하지 않는 방입니다."
            })
            return
        # 요청한 사용자가 해당 방 멤버인지 확인
        if id not in room["member"]:
            send_message(client_socket, {
                "type": "invite_member_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "member": [],
                "message": "초대 가능한 회원 목록 조회 실패: 해당 방의 참여자가 아닙니다."
            })
            return

        # 전체 회원 목록 조회
        members = self.member_repo.find_all_members()

        result = []
        for member in members:
            member_id = member.get("id", "")
            nickname = member.get("nickname", "")
            # 이미 방에 있는 회원은 제외
            if member_id in room["member"]:
                continue
            # 접속 상태 확인
            if member_id in self.login_clients:
                status = "online"
            else:
                status = "offline"

            result.append({
                "id": member_id,
                "nickname": nickname,
                "status": status
            })

        send_message(client_socket, {
            "type": "invite_member_list",
            "success": True,
            "room_id": room_id,
            "id": id,
            "member": result,
            "message": "초대 가능한 회원 목록 조회 성공"
        })

    # 방 생성용 회원 목록 조회 처리
    def handle_room_member_list(self, client_socket, message):
        id = message.get("id")

        # 사용자 ID 검사
        if id is None or id.strip() == "":
            send_message(client_socket, {
                "type": "room_member_list",
                "success": False,
                "id": id,
                "member": [],
                "message": "방 생성용 회원 목록 조회 실패: 사용자 ID가 없습니다."
            })
            return

        # 전체 회원 목록 조회
        members = self.member_repo.find_all_members()

        result = []

        for member in members:
            member_id = member.get("id", "")
            nickname = member.get("nickname", "")
            # 자기 자신은 제외
            if member_id == id:
                continue
            # 접속 상태 확인
            if member_id in self.login_clients:
                status = "online"
            else:
                status = "offline"

            result.append({
                "id": member_id,
                "nickname": nickname,
                "status": status
            })

        send_message(client_socket, {
            "type": "room_member_list",
            "success": True,
            "id": id,
            "member": result,
            "message": "방 생성용 회원 목록 조회 성공"
        })

if __name__ == "__main__":
    server = ChatServer()
    server.start()