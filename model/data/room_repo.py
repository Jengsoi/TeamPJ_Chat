import json
import os


class RoomRepository:
    def __init__(self):
        self.file_path = "data/room.json"
        self.create_file_if_not_exists()

    # room.json 파일과 data 폴더가 없으면 생성
    def create_file_if_not_exists(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({"room": []}, file, ensure_ascii=False, indent=4)

    # 채팅방 정보를 불러오는 함수
    def load_rooms(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            data = {"room": []}

        except json.JSONDecodeError:
            data = {"room": []}

        if "room" not in data:
            data["room"] = []

        return data

    # 채팅방 정보를 JSON 파일에 저장
    def save_rooms(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 새로운 채팅방 추가
    def add_room(self, room):
        data = self.load_rooms()
        data["room"].append(room)
        self.save_rooms(data)

    # 다음 채팅방 번호 생성
    def get_next_room_id(self):
        data = self.load_rooms()

        if len(data["room"]) == 0:
            return 1

        max_room_id = 0

        for room in data["room"]:
            if "room_id" in room and max_room_id < room["room_id"]:
                max_room_id = room["room_id"]

        return max_room_id + 1

    # room_id로 채팅방 하나 검색
    def find_room_by_id(self, room_id):
        data = self.load_rooms()

        for room in data["room"]:
            if room["room_id"] == room_id:
                return room

        return None

    # 사용자가 참여한 채팅방 목록 조회
    def find_rooms_by_user_id(self, id):
        data = self.load_rooms()
        result = []

        for room in data["room"]:
            if "member" in room and id in room["member"]:
                result.append(room)

        return result

    # 채팅방에서 사용자 제거
    def remove_user_from_room(self, room_id, id):
        data = self.load_rooms()

        for room in data["room"]:
            if room["room_id"] == room_id:

                if "member" not in room:
                    return False

                if id in room["member"]:
                    index = room["member"].index(id)

                    room["member"].pop(index)

                    if "nickname" in room and len(room["nickname"]) > index:
                        room["nickname"].pop(index)

                    self.save_rooms(data)
                    return True

        return False

    # 채팅방에 사용자 초대
    def add_user_to_room(self, room_id, id, nickname):
        data = self.load_rooms()

        for room in data["room"]:
            if room["room_id"] == room_id:
                if "member" not in room:
                    room["member"] = []
                if "nickname" not in room:
                    room["nickname"] = []
                if id in room["member"]:
                    return False
                room["member"].append(id)
                room["nickname"].append(nickname)

                self.save_rooms(data)
                return True

        return False