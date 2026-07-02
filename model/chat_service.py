from datetime import datetime

from room_repo import RoomRepository
from chat_repo import ChatRepository

class ChatService:
    def __init__(self):
        self.room_repo = RoomRepository()
        self.chat_repo = ChatRepository()

    # 현재 시간을 시:분:초 형식으로 반환
    def get_now_time(self):
        return datetime.now().strftime("%H:%M:%S")

    # room_id를 숫자로 변환
    def convert_room_id(self, room_id):
        try:
            return int(room_id)
        except (TypeError, ValueError):
            return None

    # 채팅 메시지 전송 함수
    def send_chat(self, room_id, id, nickname, content):
        room_id = self.convert_room_id(room_id)

        if room_id is None:
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 방 번호가 올바르지 않습니다."
            }
        if id is None or id.strip() == "":
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 사용자 ID가 없습니다."
            }
        if nickname is None or nickname.strip() == "":
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 닉네임이 없습니다."
            }
        if content is None or content.strip() == "":
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 빈 메시지는 보낼 수 없습니다."
            }

        room = self.room_repo.find_room_by_id(room_id)

        if room is None:
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 존재하지 않는 방입니다."
            }
        if id not in room["member"]:
            return {
                "type": "message",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "메시지 전송 실패: 해당 방의 참여자가 아닙니다."
            }

        created_at = self.get_now_time()

        chat = {
            "room_id": room_id,
            "id": id,
            "nickname": nickname,
            "content": content,
            "created_at": created_at
        }

        self.chat_repo.add_chat(chat)

        return {
            "type": "message",
            "success": True,
            "room_id": room_id,
            "id": id,
            "nickname": nickname,
            "content": content,
            "created_at": created_at,
            "member": room["member"],
            "message": "메시지 전송 성공"
        }

    # 채팅 기록 조회 함수
    def get_chat_list(self, room_id, id):
        room_id = self.convert_room_id(room_id)

        if room_id is None:
            return {
                "type": "chat_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "chat": [],
                "message": "채팅 기록 조회 실패: 방 번호가 올바르지 않습니다."
            }
        if id is None or id.strip() == "":
            return {
                "type": "chat_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "chat": [],
                "message": "채팅 기록 조회 실패: 사용자 ID가 없습니다."
            }

        room = self.room_repo.find_room_by_id(room_id)

        if room is None:
            return {
                "type": "chat_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "chat": [],
                "message": "채팅 기록 조회 실패: 존재하지 않는 방입니다."
            }
        if id not in room["member"]:
            return {
                "type": "chat_list",
                "success": False,
                "room_id": room_id,
                "id": id,
                "chat": [],
                "message": "채팅 기록 조회 실패: 해당 방의 참여자가 아닙니다."
            }

        chats = self.chat_repo.find_chats_by_room_id(room_id)

        return {
            "type": "chat_list",
            "success": True,
            "room_id": room_id,
            "id": id,
            "chat": chats,
            "message": "채팅 기록 조회 성공"
        }