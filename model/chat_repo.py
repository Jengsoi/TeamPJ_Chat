import json
import os

class ChatRepository:
    # 객체 생성 시 chat.json 파일 경로를 설정하고 파일이 없으면 생성
    def __init__(self):
        self.file_path = "data/chat.json"
        self.create_file_if_not_exists()

    # chat.json 파일과 data 폴더가 없으면 생성
    def create_file_if_not_exists(self):
        # data 폴더가 없으면 생성
        if not os.path.exists("data"):
            os.makedirs("data")
        # chat.json 파일이 없으면 기본 구조 생성
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({"chat": []}, file, ensure_ascii=False, indent=4)

    # 채팅 메시지 불러오기
    def load_chats(self):
        try:
            # chat.json 파일 열기
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        # 파일이 없으면 빈 데이터 생성
        except FileNotFoundError:
            data = {"chat": []}
        # JSON 형식이 잘못되어 있으면 빈 데이터 생성
        except json.JSONDecodeError:
            data = {"chat": []}
        # chat 키가 없으면 생성
        if "chat" not in data:
            data["chat"] = []
        return data

    # 채팅 메시지 저장
    def save_chats(self, data):
        # chat.json 파일에 저장
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 새로운 채팅 메시지 추가
    def add_chat(self, chat):
        # 기존 채팅 데이터 불러오기
        data = self.load_chats()
        # 새로운 채팅 메시지 추가
        data["chat"].append(chat)
        # 변경된 데이터 저장
        self.save_chats(data)

    # 특정 방의 채팅 메시지 조회
    def find_chats_by_room_id(self, room_id):
        # 채팅 데이터 불러오기
        data = self.load_chats()
        # 조회 결과를 저장할 리스트
        result = []

        # 같은 room_id를 가진 채팅 메시지 찾기
        for chat in data["chat"]:
            if chat["room_id"] == room_id:
                result.append(chat)
        # 조회 결과 반환
        return result

