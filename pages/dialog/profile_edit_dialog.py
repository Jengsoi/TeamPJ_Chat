# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_edit_dialog.ui'
## Generated for PySide6 by fallback converter.
################################################################################

from PySide6 import QtCore, QtWidgets


class Ui_profile_edit_dialog(object):
    def setupUi(self, profileeditdialog):
        profileeditdialog.setObjectName('profileeditdialog')
        profileeditdialog.resize(360, 300)
        profileeditdialog.setWindowTitle('Dialog')
        self.profileframe = QtWidgets.QFrame(profileeditdialog)
        self.profileframe.setObjectName('profileframe')
        self.profileframe.setGeometry(QtCore.QRect(0, 0, 360, 300))
        self.profileframe.setStyleSheet('#profileframe{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n}')
        self.profileframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.profileframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.profileframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(30, 20, 300, 30))
        self.titlelabel.setStyleSheet('#titlelabel{\n    background:transparent;\n    color:#111827;\n    font-size:17px;\n    font-weight:bold;\n}')
        self.titlelabel.setText('프로필 정보 변경')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nicknameinput = QtWidgets.QLineEdit(self.profileframe)
        self.nicknameinput.setObjectName('nicknameinput')
        self.nicknameinput.setGeometry(QtCore.QRect(40, 80, 280, 40))
        self.nicknameinput.setStyleSheet('#nicknameinput{\n    background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n}')
        self.nicknameinput.setPlaceholderText('닉네임 입력')
        self.nicknameinput.clear()
        self.statusinput = QtWidgets.QLineEdit(self.profileframe)
        self.statusinput.setObjectName('statusinput')
        self.statusinput.setGeometry(QtCore.QRect(40, 140, 280, 40))
        self.statusinput.setStyleSheet('#statusinput{\n    background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    padding-left:10px;\n}')
        self.statusinput.setPlaceholderText('상태메세지 입력')
        self.statusinput.clear()
        self.savebutton = QtWidgets.QPushButton(self.profileframe)
        self.savebutton.setObjectName('savebutton')
        self.savebutton.setGeometry(QtCore.QRect(40, 220, 130, 42))
        self.savebutton.setStyleSheet('#savebutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:8px;\n    font-weight:bold;\n}')
        self.savebutton.setText('저장')
        self.cancelbutton = QtWidgets.QPushButton(self.profileframe)
        self.cancelbutton.setObjectName('cancelbutton')
        self.cancelbutton.setGeometry(QtCore.QRect(190, 220, 130, 42))
        self.cancelbutton.setStyleSheet('#cancelbutton{\n    background:#ffffff;\n    color:#6b7280;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n}')
        self.cancelbutton.setText('취소')

        self.retranslateui(profileeditdialog)
        QtCore.QMetaObject.connectSlotsByName(profileeditdialog)

    def retranslateui(self, profileeditdialog):
        pass
