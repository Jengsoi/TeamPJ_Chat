# 💬 TCP/IP 채팅 시스템

Python 기반의 **Client-Server 채팅 프로그램**입니다.

TCP/IP Socket을 이용해 여러 사용자가 서버에 접속하고,  
회원가입과 로그인, 채팅방 생성, 메시지 전송, 귓속말 등의 기능을 사용할 수 있도록 구현했습니다.

팀 프로젝트에서 **서버 개발을 담당**했으며,  
클라이언트의 요청 처리부터 채팅방 관리, 메시지 전달, 데이터 저장 구조를 구현했습니다.

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|---|---|
| 프로젝트 형태 | 팀 프로젝트 |
| 담당 역할 | Server 개발 |
| 개발 언어 | Python |
| 통신 방식 | TCP/IP Socket |
| 데이터 형식 | JSON |
| 메시지 프레이밍 | 4Byte Header |
| 데이터 저장 | JSON File |

---

## 🛠 Tech Stack

### Language

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### Communication & Data

![TCP/IP](https://img.shields.io/badge/TCP%2FIP-005571?style=flat-square)
![Socket](https://img.shields.io/badge/Socket-333333?style=flat-square)
![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white)

### Development Tools

![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=pycharm&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)

---

## 🏗 System Architecture

```text
┌──────────────┐
│   Client A   │
└──────┬───────┘
       │
       │ TCP/IP Socket
       │
┌──────▼───────────────────────────────┐
│               Server                 │
│                                      │
│  ┌───────────────┐                   │
│  │    Server     │                   │
│  │ Client 관리   │                   │
│  └───────┬───────┘                   │
│          │                            │
│  ┌───────▼────────┐                  │
│  │ ClientHandler  │                  │
│  │ 요청 수신/분기 │                  │
│  └───────┬────────┘                  │
│          │                            │
│  ┌───────▼────────┐                  │
│  │  ChatService   │                  │
│  │ 방/메시지 관리 │                  │
│  └───────┬────────┘                  │
│          │                            │
│  ┌───────▼────────────────────────┐  │
│  │ Repository / JSON Storage      │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
       │
       │ TCP/IP Socket
       │
┌──────▼───────┐
│   Client B   │
└──────────────┘
```

서버에서 클라이언트의 연결을 관리하고,  
각 클라이언트의 요청을 `ClientHandler`에서 구분하여 처리하도록 구성했습니다.

채팅방과 메시지 관련 로직은 별도의 서비스 영역으로 분리하고,  
사용자와 채팅 데이터는 JSON 파일을 통해 저장했습니다.

---

## ✨ 주요 기능

### 👤 회원 관리

- 회원가입
- 로그인
- 사용자 프로필 수정
- 사용자 정보 저장

### 💬 채팅

- 실시간 메시지 송수신
- 채팅방별 메시지 전달
- 귓속말
- 시스템 메시지 처리

### 🚪 채팅방

- 채팅방 생성
- 채팅방 입장
- 채팅방 퇴장
- 채팅방 사용자 관리

### 📁 데이터 관리

- 회원 정보 저장
- 채팅방 정보 저장
- 채팅 메시지 저장
- JSON 기반 데이터 관리

---

## 🔌 Communication Protocol

클라이언트와 서버는 **JSON 형태의 메시지**를 주고받습니다.

TCP는 메시지의 경계를 보장하지 않기 때문에  
JSON 데이터 앞에 **고정 4Byte Header**를 추가하여 메시지 길이를 전달하도록 구현했습니다.

```text
┌──────────────┬───────────────────────────────┐
│ 4Byte Header │         JSON Payload          │
│ Message Size │                               │
└──────────────┴───────────────────────────────┘
```

### 메시지 예시

```json
{
    "type": "message",
    "room_id": 1,
    "sender_id": 3,
    "nickname": "user01",
    "content": "안녕하세요.",
    "created_at": "2026-06-01 15:30:00"
}
```

---

## 📡 주요 요청 Type

서버에서는 클라이언트가 전달한 `type` 값을 기준으로 요청을 구분합니다.

| Type | 기능 |
|---|---|
| `register` | 회원가입 |
| `login` | 로그인 |
| `room` | 채팅방 생성 |
| `join_room` | 채팅방 입장 |
| `out_room` | 채팅방 퇴장 |
| `message` | 메시지 전송 |
| `whisper` | 귓속말 |
| `update_profile` | 프로필 수정 |
| `file` | 파일 관련 요청 |
| `error` | 오류 메시지 |
| `system` | 시스템 메시지 |

---

## 🖥 담당 역할

팀 프로젝트에서 **서버 영역을 담당**했습니다.

### Server

- TCP Socket 생성 및 연결 대기
- 여러 Client 연결 관리
- 접속한 Client 목록 관리
- 채팅방별 메시지 Broadcast
- 서버 종료 시 연결 정리

### ClientHandler

- Client별 데이터 수신
- 4Byte Header 분석
- JSON Payload 변환
- 요청 `type`에 따른 기능 분기
- 비정상 연결 처리

### ChatService

- 채팅방 관리
- 메시지 처리
- 입장 / 퇴장 관리
- 귓속말 처리

### Repository

- Member 데이터 관리
- Room 데이터 관리
- Chat 데이터 관리
- JSON 데이터 저장 및 조회

---

## 💾 Data Storage

별도의 데이터베이스 대신 JSON 파일을 사용하여  
회원, 채팅방, 메시지 데이터를 관리했습니다.

```text
Storage
├── members.json
├── room.json
└── chat.json
```

각 데이터에서는 사용자 및 채팅방을 구분하기 위해  
고유한 `id`를 사용하도록 데이터 구조를 통일했습니다.

---

## 🔍 구현하면서 고민한 부분

### 1. TCP 메시지 경계 문제

TCP 통신에서는 한 번 전송한 데이터가  
한 번의 `recv()`에서 동일한 크기로 들어온다는 보장이 없습니다.

따라서 JSON 데이터 앞에 4Byte Header를 붙이고  
Header에 Payload 크기를 기록하여 필요한 길이만큼 데이터를 수신하도록 구성했습니다.

```text
Header 확인
    ↓
Payload 길이 확인
    ↓
필요한 데이터가 모두 들어올 때까지 수신
    ↓
JSON 변환
    ↓
요청 처리
```

---

### 2. 서버 역할 분리

처음에는 서버에서 연결 관리와 요청 처리, 채팅 로직을 모두 담당하면  
코드가 복잡해질 수 있었습니다.

역할을 다음과 같이 분리했습니다.

```text
Server
  └─ 연결 관리

ClientHandler
  └─ 요청 수신 및 분기

ChatService
  └─ 채팅 관련 비즈니스 로직

Repository
  └─ 데이터 저장 및 조회
```

이를 통해 각 클래스가 담당하는 역할을 구분하고  
기능 수정 시 영향을 받는 범위를 줄이고자 했습니다.

---

### 3. 귓속말 처리

일반 채팅은 같은 방에 있는 사용자에게 메시지를 전달하지만,  
귓속말은 지정한 사용자에게만 메시지를 전달해야 합니다.

따라서 접속 사용자 목록에서 대상 사용자를 확인한 뒤  
해당 Client에게만 메시지를 전달하도록 처리했습니다.

또한 자기 자신에게 귓속말을 보내는 경우는  
잘못된 요청으로 처리하도록 예외 조건을 추가했습니다.

---

## 💡 배운 점

이 프로젝트를 통해 단순히 Socket을 연결하는 것보다  
**통신 데이터를 어떤 형식으로 정의하고 서버에서 어떻게 처리할 것인지가 중요하다**는 것을 배웠습니다.

특히 TCP 통신 과정에서 메시지의 경계가 자동으로 구분되지 않는다는 점을 이해하면서  
4Byte Header를 이용한 메시지 프레이밍 방식을 직접 적용해볼 수 있었습니다.

또한 서버의 기능을 하나의 파일에 모두 구현하기보다는  
`Server`, `ClientHandler`, `Service`, `Repository`와 같이 역할을 구분하면서  
프로그램의 구조를 나누는 이유도 경험할 수 있었습니다.

이 프로젝트를 계기로 단순히 기능이 동작하는 것뿐 아니라  
**클라이언트의 요청이 서버에 도착한 뒤 어떤 순서로 처리되고 다시 응답되는지**  
전체 흐름을 이해하는 것이 중요하다는 것을 배웠습니다.

---

## 🎯 프로젝트를 통해 경험한 것

- TCP/IP Socket 통신
- Client-Server 구조
- 다중 Client 연결 관리
- JSON 데이터 송수신
- TCP Message Framing
- 채팅방 및 사용자 상태 관리
- 서버 구조 분리
- 예외 처리
- Git / GitHub 팀 협업

---

## 📄 License

교육 과정에서 진행한 팀 프로젝트입니다.
