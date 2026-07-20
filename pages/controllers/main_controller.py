from PySide6.QtWidgets import QMainWindow, QWidget

# 메인 윈도우(UI)
from ui_mainwindow import Ui_MainWindow

# 각 화면(UI)
from pages.login_page import Ui_login
from pages.signup_page import Ui_signup
from pages.signup_complete_page import Ui_signup_complete
from pages.main_page import Ui_main
from pages.chat_room_page import Ui_chat_room
from pages.user_list_page import Ui_user_list
from pages.chat_list_page import Ui_chat_list
from pages.setting_page import Ui_setting


# 전체 화면 전환을 담당하는 메인 컨트롤러
class MainController(QMainWindow):

    def __init__(self):
        super().__init__()

        # MainWindow UI 적용
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 각 화면(QWidget + UI) 생성
        self.create_pages()

        # 메인 스택(mainstack) 구성
        self.setup_main_stack()

        # 메인화면 내부 stackedWidget 구성
        self.setup_content_stack()

        # 버튼 시그널 연결
        self.connect_buttons()

    # -------------------------------
    # 각 페이지 생성
    # -------------------------------
    def create_pages(self):

        # 메인 Stack에 들어갈 QWidget 생성
        self.login_page = QWidget()
        self.signup_page = QWidget()
        self.signup_complete_page = QWidget()
        self.main_page = QWidget()
        self.chat_room_page = QWidget()

        # MainPage 내부 stackedWidget에 들어갈 QWidget 생성
        self.user_list_page = QWidget()
        self.chat_list_page = QWidget()
        self.setting_page = QWidget()

        # 로그인 화면 UI 적용
        self.login_ui = Ui_login()
        self.login_ui.setupUi(self.login_page)

        # 회원가입 화면 UI 적용
        self.signup_ui = Ui_signup()
        self.signup_ui.setupUi(self.signup_page)

        # 회원가입 완료 화면 UI 적용
        self.signup_complete_ui = Ui_signup_complete()
        self.signup_complete_ui.setupUi(self.signup_complete_page)

        # 메인 화면 UI 적용
        self.main_ui = Ui_main()
        self.main_ui.setupUi(self.main_page)

        # 채팅방 화면 UI 적용
        self.chat_room_ui = Ui_chat_room()
        self.chat_room_ui.setupUi(self.chat_room_page)

        # 사용자 목록 화면 UI 적용
        self.user_list_ui = Ui_user_list()
        self.user_list_ui.setupUi(self.user_list_page)

        # 채팅 목록 화면 UI 적용
        self.chat_list_ui = Ui_chat_list()
        self.chat_list_ui.setupUi(self.chat_list_page)

        # 설정 화면 UI 적용
        self.setting_ui = Ui_setting()
        self.setting_ui.setupUi(self.setting_page)

    # -------------------------------
    # MainWindow의 mainstack 구성
    # -------------------------------
    def setup_main_stack(self):

        # Qt Designer 기본 페이지 제거
        while self.ui.mainstack.count() > 0:
            widget = self.ui.mainstack.widget(0)
            self.ui.mainstack.removeWidget(widget)

        # mainstack 페이지 등록
        self.ui.mainstack.addWidget(self.login_page)             # index 0
        self.ui.mainstack.addWidget(self.signup_page)            # index 1
        self.ui.mainstack.addWidget(self.signup_complete_page)   # index 2
        self.ui.mainstack.addWidget(self.main_page)              # index 3
        self.ui.mainstack.addWidget(self.chat_room_page)         # index 4

        # 프로그램 시작 시 로그인 화면 표시
        self.ui.mainstack.setCurrentIndex(0)

    # -------------------------------
    # MainPage 내부 stackedWidget 구성
    # -------------------------------
    def setup_content_stack(self):

        # Qt creator 기본 페이지 제거
        while self.main_ui.stackedWidget.count() > 0:
            widget = self.main_ui.stackedWidget.widget(0)
            self.main_ui.stackedWidget.removeWidget(widget)

        # 메인 화면 내부 페이지 등록
        self.main_ui.stackedWidget.addWidget(self.user_list_page)   # index 0
        self.main_ui.stackedWidget.addWidget(self.chat_list_page)   # index 1
        self.main_ui.stackedWidget.addWidget(self.setting_page)     # index 2

        # 로그인 후 사용자 목록이 기본 화면
        self.main_ui.stackedWidget.setCurrentIndex(0)

    # -------------------------------
    # 버튼 클릭 이벤트 연결
    # -------------------------------
    def connect_buttons(self):

        # 로그인 화면
        self.login_ui.loginbutton.clicked.connect(self.show_main_page)
        self.login_ui.signupbutton.clicked.connect(self.show_signup_page)

        # 회원가입 화면
        self.signup_ui.signupbutton.clicked.connect(self.show_signup_complete_page)
        self.signup_ui.backloginbutton.clicked.connect(self.show_login_page)

        # 회원가입 완료 화면
        self.signup_complete_ui.loginbutton.clicked.connect(self.show_login_page)

        # 메인 화면 하단 메뉴
        self.main_ui.userbutton.clicked.connect(self.show_user_list_page)
        self.main_ui.chatbutton.clicked.connect(self.show_chat_list_page)
        self.main_ui.settingbutton.clicked.connect(self.show_setting_page)

        # 채팅방 뒤로가기
        self.chat_room_ui.backbutton.clicked.connect(self.show_main_page)

    # -------------------------------
    # 화면 전환 함수
    # -------------------------------

    # 로그인 화면
    def show_login_page(self):
        self.ui.mainstack.setCurrentIndex(0)
        #self.ui.mainstack.setCurrentIndex(1)

    # 회원가입 화면
    def show_signup_page(self):
        self.ui.mainstack.setCurrentIndex(1)

    # 회원가입 완료 화면
    def show_signup_complete_page(self):
        self.ui.mainstack.setCurrentIndex(2)

    # 메인 화면
    def show_main_page(self):
        self.ui.mainstack.setCurrentIndex(3)

        # 메인 진입 시 사용자 목록을 기본으로 표시
        self.main_ui.stackedWidget.setCurrentIndex(0)

    # 채팅방 화면
    def show_chat_room_page(self):
        self.ui.mainstack.setCurrentIndex(4)

    # 메인 > 사용자 목록
    def show_user_list_page(self):
        self.main_ui.stackedWidget.setCurrentIndex(0)

    # 메인 > 채팅 목록
    def show_chat_list_page(self):
        self.main_ui.stackedWidget.setCurrentIndex(1)

    # 메인 > 설정
    def show_setting_page(self):
        self.main_ui.stackedWidget.setCurrentIndex(2)