import json
import os

class MemberRepo:
    def __init__(self):
        self.file_path = "data/members.json"
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({"member":[]}, file, ensure_ascii=False, indent=4)

    # 회원정보 불러오기
    def load_members(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"member":[]}
        except json.JSONDecodeError:
            data = {"member":[]}
        if "member" not in data:
            data["member"] = []
        return data

    # 전체 회원 목록 조회
    def find_all_members(self):
        data = self.load_members()
        return data["member"]