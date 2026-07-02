from datetime import datetime
from room_repo import RoomRepository

class RoomService:

    # RoomService 객체 생성 시 RoomRepository 객체 생성
    def __init__(self):
        self.room_repo = RoomRepository()

    # 현재 시간을 시:분:초 형식으로 반환
    def get_now_time(self):
        return datetime.now().strftime("%H:%M:%S")

    # room_id를 숫자로 변환
    def convert_room_id(self, room_id):
        try:
            return int(room_id)

        # 숫자로 변환할 수 없으면 None 반환
        except (TypeError, ValueError):
            return None

    # 채팅방 생성 함수
    def make_room(self, ids, nicknames):
        # 선택한 사용자가 없거나 2명 미만이면 방 생성 실패
        if ids is None or len(ids) < 2:
            return {
                "type": "room",
                "success": False,
                "room_id": None,
                "member": ids,
                "nickname": nicknames,
                "message": "방 생성 실패: 사용자를 2명 이상 선택하세요."
            }
        # 닉네임 개수와 아이디 개수가 다르면 방 생성 실패
        if nicknames is None or len(nicknames) != len(ids):
            return {
                "type": "room",
                "success": False,
                "room_id": None,
                "member": ids,
                "nickname": nicknames,
                "message": "방 생성 실패: 아이디와 닉네임 개수가 일치하지 않습니다."
            }
        # 중복된 사용자가 있으면 방 생성 실패
        if len(ids) != len(set(ids)):
            return {
                "type": "room",
                "success": False,
                "room_id": None,
                "member": ids,
                "nickname": nicknames,
                "message": "방 생성 실패: 중복된 사용자가 있습니다."
            }

        # 다음 채팅방 번호 가져오기
        room_id = self.room_repo.get_next_room_id()

        # 저장할 채팅방 정보 생성
        room = {
            "room_id": room_id,
            "member": ids,
            "nickname": nicknames,
            "created_at": self.get_now_time()
        }

        # 채팅방 저장
        self.room_repo.add_room(room)

        # 방 생성 성공 결과 반환
        return {
            "type": "room",
            "success": True,
            "room_id": room_id,
            "member": ids,
            "nickname": nicknames,
            "room": room,
            "message": "방 생성 성공"
        }

    # 채팅방 목록 조회 함수
    def get_room_list(self, id):
        # 사용자 ID가 없으면 조회 실패
        if id is None or id.strip() == "":
            return {
                "type": "room_list",
                "success": False,
                "id": id,
                "room": [],
                "message": "채팅방 목록 조회 실패: 사용자 ID가 없습니다."
            }

        # 사용자가 참여한 채팅방 목록 조회
        rooms = self.room_repo.find_rooms_by_user_id(id)

        # 조회 성공 결과 반환
        return {
            "type": "room_list",
            "success": True,
            "id": id,
            "room": rooms,
            "message": "채팅방 목록 조회 성공"
        }

    # 채팅방 입장 함수
    def join_room(self, room_id, id):
        # room_id를 숫자로 변환
        room_id = self.convert_room_id(room_id)

        # 방 번호가 올바르지 않으면 입장 실패
        if room_id is None:
            return {
                "type": "join_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "입장 실패: 방 번호가 올바르지 않습니다."
            }
        # 사용자 ID가 없으면 입장 실패
        if id is None or id.strip() == "":
            return {
                "type": "join_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "입장 실패: 사용자 ID가 없습니다."
            }

        # room_id에 해당하는 채팅방 조회
        room = self.room_repo.find_room_by_id(room_id)

        # 채팅방이 존재하지 않으면 입장 실패
        if room is None:
            return {
                "type": "join_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "입장 실패: 존재하지 않는 방입니다."
            }
        # 사용자가 채팅방 참여자가 아니면 입장 실패
        if id not in room["member"]:
            return {
                "type": "join_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "입장 실패: 해당 방의 참여자가 아닙니다."
            }

        # 입장 성공 결과 반환
        return {
            "type": "join_room",
            "success": True,
            "room_id": room_id,
            "id": id,
            "room": room,
            "message": "입장"
        }

    # 채팅방 나가기 함수
    def out_room(self, room_id, id):
        # room_id를 숫자로 변환
        room_id = self.convert_room_id(room_id)
        # 방 번호가 올바르지 않으면 나가기 실패
        if room_id is None:
            return {
                "type": "out_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "나가기 실패: 방 번호가 올바르지 않습니다."
            }
        # 사용자 ID가 없으면 나가기 실패
        if id is None or id.strip() == "":
            return {
                "type": "out_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "나가기 실패: 사용자 ID가 없습니다."
            }

        # room_id에 해당하는 채팅방 조회
        room = self.room_repo.find_room_by_id(room_id)

        # 채팅방이 존재하지 않으면 나가기 실패
        if room is None:
            return {
                "type": "out_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "나가기 실패: 존재하지 않는 방입니다."
            }
        # 사용자가 채팅방 참여자가 아니면 나가기 실패
        if id not in room["member"]:
            return {
                "type": "out_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "나가기 실패: 해당 방의 참여자가 아닙니다."
            }

        # 채팅방에서 사용자 제거
        success = self.room_repo.remove_user_from_room(room_id, id)

        # 사용자 제거에 실패하면 나가기 실패
        if not success:
            return {
                "type": "out_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "나가기 실패"
            }

        # 변경된 채팅방 정보 다시 조회
        room = self.room_repo.find_room_by_id(room_id)

        # 남은 멤버 목록 저장
        members = []

        # 채팅방이 존재하고 member 키가 있으면 남은 멤버 목록 저장
        if room is not None and "member" in room:
            members = room["member"]
        # 나가기 성공 결과 반환
        return {
            "type": "out_room",
            "success": True,
            "room_id": room_id,
            "id": id,
            "room": room,
            "member": members,
            "message": "방 나감"
        }

    # 채팅방 친구 초대 함수
    def invite_room(self, room_id, id, nickname):
        # room_id를 숫자로 변환
        room_id = self.convert_room_id(room_id)

        # 방 번호가 올바르지 않으면 초대 실패
        if room_id is None:
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패: 방 번호가 올바르지 않습니다."
            }
        # 초대할 사용자 ID가 없으면 초대 실패
        if id is None or id.strip() == "":
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패: 초대할 사용자 ID가 없습니다."
            }
        # 초대할 사용자 닉네임이 없으면 초대 실패
        if nickname is None or nickname.strip() == "":
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패: 초대할 사용자 닉네임이 없습니다."
            }
        # room_id에 해당하는 채팅방 조회
        room = self.room_repo.find_room_by_id(room_id)

        # 채팅방이 존재하지 않으면 초대 실패
        if room is None:
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패: 존재하지 않는 방입니다."
            }
        # 이미 채팅방에 있는 사용자면 초대 실패
        if id in room["member"]:
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패: 이미 채팅방에 있는 사용자입니다."
            }

        # 채팅방에 사용자 추가
        success = self.room_repo.add_user_to_room(room_id, id, nickname)

        # 사용자 추가에 실패하면 초대 실패
        if not success:
            return {
                "type": "invite_room",
                "success": False,
                "room_id": room_id,
                "id": id,
                "message": "친구 초대 실패"
            }

        # 변경된 채팅방 정보 다시 조회
        room = self.room_repo.find_room_by_id(room_id)

        # 초대 성공 결과 반환
        return {
            "type": "invite_room",
            "success": True,
            "room_id": room_id,
            "id": id,
            "nickname": nickname,
            "room": room,
            "member": room["member"],
            "message": "친구 초대 성공"
        }