# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_edit_dialog.ui'
## Generated for PySide6 by fallback converter.
################################################################################

from PySide6 import QtCore, QtWidgets


class Ui_account_edit_dialog(object):
    def setupUi(self, profile_edit_dialog):
        profile_edit_dialog.setObjectName('profile_edit_dialog')
        profile_edit_dialog.resize(360, 560)
        profile_edit_dialog.setWindowTitle('Dialog')
        self.frame = QtWidgets.QFrame(profile_edit_dialog)
        self.frame.setObjectName('frame')
        self.frame.setGeometry(QtCore.QRect(0, 0, 360, 560))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.frame)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(40, 20, 300, 38))
        self.titlelabel.setStyleSheet('#titlelabel{\n    background:transparent;\n    color:#111827;\n    font-size:17px;\n    font-weight:bold;\n}')
        self.titlelabel.setText('회원 정보 변경')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nicknameinput = QtWidgets.QLineEdit(self.frame)
        self.nicknameinput.setObjectName('nicknameinput')
        self.nicknameinput.setGeometry(QtCore.QRect(40, 75, 280, 40))
        self.nicknameinput.setStyleSheet('#nicknameinput{\n    background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n}\n')
        self.nicknameinput.setPlaceholderText('사번 입력')
        self.nicknameinput.clear()
        self.statusinput = QtWidgets.QLineEdit(self.frame)
        self.statusinput.setObjectName('statusinput')
        self.statusinput.setGeometry(QtCore.QRect(40, 125, 280, 40))
        self.statusinput.setStyleSheet('#statusinput{\n    background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n}')
        self.statusinput.setPlaceholderText('이름')
        self.statusinput.clear()
        self.savebutton = QtWidgets.QPushButton(self.frame)
        self.savebutton.setObjectName('savebutton')
        self.savebutton.setGeometry(QtCore.QRect(40, 400, 130, 42))
        self.savebutton.setStyleSheet('#savebutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:8px;\n    font-weight:bold;\n}')
        self.savebutton.setText('저장')
        self.savebutton.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cancelbutton = QtWidgets.QPushButton(self.frame)
        self.cancelbutton.setObjectName('cancelbutton')
        self.cancelbutton.setGeometry(QtCore.QRect(200, 400, 130, 42))
        self.cancelbutton.setStyleSheet('#cancelbutton{\n    background:#ffffff;\n    color:#6b7280;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n}')
        self.cancelbutton.setText('취소')
        self.cancelbutton.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.phoneinput = QtWidgets.QLineEdit(self.frame)
        self.phoneinput.setObjectName('phoneinput')
        self.phoneinput.setGeometry(QtCore.QRect(40, 175, 280, 40))
        self.phoneinput.setStyleSheet(' background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n')
        self.phoneinput.setPlaceholderText('핸드폰 번호')
        self.phoneinput.clear()
        self.idinput = QtWidgets.QLineEdit(self.frame)
        self.idinput.setObjectName('idinput')
        self.idinput.setGeometry(QtCore.QRect(40, 225, 280, 40))
        self.idinput.setStyleSheet(' background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n')
        self.idinput.setPlaceholderText('아이디')
        self.idinput.clear()
        self.pwinput = QtWidgets.QLineEdit(self.frame)
        self.pwinput.setObjectName('pwinput')
        self.pwinput.setGeometry(QtCore.QRect(40, 275, 280, 40))
        self.pwinput.setStyleSheet(' background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n')
        self.pwinput.setPlaceholderText('비밀번호')
        self.pwinput.clear()
        self.pwcheckinput = QtWidgets.QLineEdit(self.frame)
        self.pwcheckinput.setObjectName('pwcheckinput')
        self.pwcheckinput.setGeometry(QtCore.QRect(40, 325, 280, 40))
        self.pwcheckinput.setStyleSheet(' background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n')
        self.pwcheckinput.setPlaceholderText('비밀번호 확인')
        self.pwcheckinput.clear()

        self.retranslateui(profile_edit_dialog)
        QtCore.QMetaObject.connectSlotsByName(profile_edit_dialog)

    def retranslateui(self, profile_edit_dialog):
        pass
