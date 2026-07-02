# 단순응용형 (protocol.py) send_message, receive_message / 송수신 메세지 활용시
# 구현기능 포함요소: 소켓통신 및 파일전송 프로토콜 모듈,JSON 기반 메시지 송수신, Base64 기반 파일 인코딩/디코딩 및 송수신, 예외 오류처리 포함

import json
import base64
import os
import socket
from typing import Tuple, List, Dict, Any, Optional

ENCODING = "utf-8"
DELIMITER = "\n"


def send_message(sock: socket.socket, message: Dict[str, Any]) -> bool:
    # 딕셔너리 형태의 메시지를 JSON으로 변환하여 소켓으로 전송한다.

    try:
        json_text = json.dumps(message, ensure_ascii=False)
        data = json_text + DELIMITER
        sock.sendall(data.encode(ENCODING))
        return True
    except socket.error as e:
        print(f"[오류] 서버로 데이터를 전송하는데 실패했습니다: {e}")
        return False
    except Exception as e:
        print(f"[오류] 알 수 없는 전송 오류가 발생했습니다: {e}")
        return False


def receive_messages(sock: socket.socket, buffer: str) -> Tuple[str, List[Dict[str, Any]], bool]:
    # 소켓으로부터 데이터를 수신하여 완전한 JSON 메세지 리스트로 반환한다.
    try:
        data = sock.recv(4096)
        if not data:
            return buffer, [], False
        buffer += data.decode(ENCODING)
        messages = []
        while DELIMITER in buffer:
            raw_message, buffer = buffer.split(DELIMITER, 1)
            if raw_message.strip():
                try:
                    message = json.loads(raw_message)
                    messages.append(message)
                except json.JSONDecodeError:
                    print("[오류] 수신된 데이터의 JSON 형식이 올바르지 않습니다.")
        return buffer, messages, True
    except ConnectionResetError:
        print("[오류] 상대방과의 연결이 끊어졌습니다.")
        return buffer, [], False
    except Exception as e:
        print(f"[오류] 메시지 수신 중 오류가 발생했습니다: {e}")
        return buffer, [], False


def send_file(sock: socket.socket, filepath: str) -> bool:
    # 사용자가 선택한 파일을 읽어 Base64로 변환한 뒤 서버로 전송한다.
    # 1. 파일 미선택 처리
    if not filepath:
        print("[안내] 전송할 파일이 선택되지 않았습니다.")
        return False

    # 파일 존재 여부 확인
    if not os.path.exists(filepath):
        print(f"[오류] 해당 경로에 파일이 존재하지 않습니다: {filepath}")
        return False

    # 2. 파일 정보 추출 및 빈 파일 처리
    filesize = os.path.getsize(filepath)
    if filesize == 0:
        print("[오류] 내용이 없는 빈 파일은 전송할 수 없습니다.")
        return False

    filename = os.path.basename(filepath)

    try:
        # 3. 파일을 Base64로 변환
        with open(filepath, "rb") as f:
            file_data = f.read()

        encoded_data = base64.b64encode(file_data).decode('utf-8')

        # 4. 파일 메시지 구성
        message = {
            "type": "file",
            "filename": filename,
            "size": filesize,
            "data": encoded_data
        }

        # 5. 파일 정보 표시 및 서버 전송
        print(f"[발신] 파일 전송을 시작합니다... (파일명: {filename}, 크기: {filesize} bytes)")

        is_success = send_message(sock, message)

        if is_success:
            print("[안내] 파일 전송이 성공적으로 완료되었습니다.")
        else:
            print("[오류] 파일 전송에 실패했습니다.")

        return is_success

    except Exception as e:
        print(f"[오류] 파일 처리 및 전송 과정에서 치명적인 오류가 발생했습니다: {e}")
        return False


def receive_file(message: Dict[str, Any], save_dir: str = "./downloads") -> bool:
    # 수신된 파일 메세지를 디코딩하여 로컬 디렉토리에 저장

    if message.get("type") != "file":
        return False

    filename = message.get("filename", "unknown_file")
    filesize = message.get("size", 0)
    encoded_data = message.get("data", "")

    # 파일 정보 표시
    print(f"[수신] 파일을 수신했습니다. (파일명: {filename}, 크기: {filesize} bytes)")

    try:
        # 저장 디렉토리 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_path = os.path.join(save_dir, filename)

        # Base64 디코딩 및 파일 저장
        file_data = base64.b64decode(encoded_data)

        with open(save_path, "wb") as f:
            f.write(file_data)

        print(f"[안내] 파일이 성공적으로 저장되었습니다: {save_path}")
        return True

    except base64.binascii.Error:
        print("[오류] 수신된 파일의 Base64 디코딩에 실패했습니다. 데이터가 손상되었을 수 있습니다.")
        return False
    except Exception as e:
        print(f"[오류] 파일 저장 중 오류가 발생했습니다: {e}")
        return False
