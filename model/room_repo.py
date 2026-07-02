import json
import os

class RoomRepository:
    # 객체 생성 시 room.json 파일 경로를 설정하고 파일이 없으면 생성
    def __init__(self):
        self.file_path = "data/room.json"
        self.create_file_if_not_exists()

    # room.json 파일과 data 폴더가 없으면 생성
    def create_file_if_not_exists(self):
        # data 폴더가 없으면 생성
        if not os.path.exists("data"):
            os.makedirs("data")
        # room.json 파일이 없으면 기본 구조 생성
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({"room": []}, file, ensure_ascii=False, indent=4)

    # 채팅방 정보를 불러오는 함수
    def load_rooms(self):
        try:
            # room.json 파일 열기
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        # 파일이 없으면 기본 데이터 생성
        except FileNotFoundError:
            data = {"room": []}
        # JSON 형식이 잘못되면 기본 데이터 생성
        except json.JSONDecodeError:
            data = {"room": []}
        # room 키가 없으면 생성
        if "room" not in data:
            data["room"] = []
        return data

    # 채팅방 정보를 JSON 파일에 저장
    def save_rooms(self, data):
        # room.json 파일에 저장
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 새로운 채팅방 추가
    def add_room(self, room):
        # 기존 채팅방 데이터 불러오기
        data = self.load_rooms()
        # room 목록에 새 채팅방 추가
        data["room"].append(room)
        # 변경된 데이터 저장
        self.save_rooms(data)

    # 다음 채팅방 번호 생성
    def get_next_room_id(self):
        # 채팅방 데이터 불러오기
        data = self.load_rooms()
        # 채팅방이 없으면 1번부터 시작
        if len(data["room"]) == 0:
            return 1
        # 가장 큰 room_id를 저장할 변수
        max_room_id = 0
        # 저장된 채팅방 중 가장 큰 room_id 찾기
        for room in data["room"]:
            if "room_id" in room and max_room_id < room["room_id"]:
                max_room_id = room["room_id"]
        # 가장 큰 room_id보다 1 큰 값 반환
        return max_room_id + 1

    # room_id로 채팅방 하나 검색
    def find_room_by_id(self, room_id):
        # 채팅방 데이터 불러오기
        data = self.load_rooms()

        # room_id가 같은 채팅방 찾기
        for room in data["room"]:
            if room["room_id"] == room_id:
                return room
        # 찾지 못하면 None 반환
        return None

    # 사용자가 참여한 채팅방 목록 조회
    def find_rooms_by_user_id(self, id):
        # 채팅방 데이터 불러오기
        data = self.load_rooms()
        # 결과를 저장할 리스트
        result = []

        # 사용자가 포함된 채팅방 찾기
        for room in data["room"]:
            if "member" in room and id in room["member"]:
                result.append(room)
        # 조회 결과 반환
        return result

    # 채팅방에서 사용자 제거
    def remove_user_from_room(self, room_id, id):
        # 채팅방 데이터 불러오기
        data = self.load_rooms()

        # 전체 채팅방 확인
        for room in data["room"]:
            # room_id가 같은 채팅방 찾기
            if room["room_id"] == room_id:
                # member 키가 없으면 제거 실패
                if "member" not in room:
                    return False
                # 사용자가 채팅방에 포함되어 있는지 확인
                if id in room["member"]:
                    # 사용자 위치 찾기
                    index = room["member"].index(id)
                    # 사용자 ID 삭제
                    room["member"].pop(index)
                    # 닉네임도 같은 위치에서 삭제
                    if "nickname" in room and len(room["nickname"]) > index:
                        room["nickname"].pop(index)
                    # 변경된 데이터 저장
                    self.save_rooms(data)
                    # 제거 성공
                    return True
        # 제거할 사용자가 없으면 실패
        return False

    # 채팅방에 사용자 초대
    def add_user_to_room(self, room_id, id, nickname):
        # 채팅방 데이터 불러오기
        data = self.load_rooms()

        # 전체 채팅방 확인
        for room in data["room"]:
            # room_id가 같은 채팅방 찾기
            if room["room_id"] == room_id:
                # member 키가 없으면 생성
                if "member" not in room:
                    room["member"] = []
                # nickname 키가 없으면 생성
                if "nickname" not in room:
                    room["nickname"] = []
                # 이미 채팅방에 있는 사용자면 실패
                if id in room["member"]:
                    return False
                # 사용자 ID 추가
                room["member"].append(id)
                # 사용자 닉네임 추가
                room["nickname"].append(nickname)
                # 변경된 데이터 저장
                self.save_rooms(data)
                # 초대 성공
                return True
        # 해당 채팅방이 없으면 실패
        return False