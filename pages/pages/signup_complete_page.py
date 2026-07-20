# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_complete_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_signup_complete(object):
    def setupUi(self, signup_complete):
        if not signup_complete.objectName():
            signup_complete.setObjectName('signup_complete_page')
        signup_complete.resize(500, 800)
        signup_complete.setStyleSheet('background:#f8fafc;')
        self.completeframe = QtWidgets.QFrame(signup_complete)
        self.completeframe.setObjectName('completeframe')
        self.completeframe.setGeometry(QtCore.QRect(60, 170, 380, 400))
        self.completeframe.setStyleSheet('#completeframe{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n}')
        self.completeframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.completeframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.checklabel = QtWidgets.QLabel(self.completeframe)
        self.checklabel.setObjectName('checklabel')
        self.checklabel.setGeometry(QtCore.QRect(130, 70, 120, 90))
        self.checklabel.setStyleSheet('#checklabel{\n    color:#2563eb;\n    background:transparent;\n    font-size:64px;\n    font-weight:bold;\n}')
        self.titlelabel = QtWidgets.QLabel(self.completeframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(40, 175, 300, 35))
        self.titlelabel.setStyleSheet('#titlelabel{\n    color:#111827;\n    background:transparent;\n    font-size:22px;\n    font-weight:bold;\n}')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subtitlelabel = QtWidgets.QLabel(self.completeframe)
        self.subtitlelabel.setObjectName('subtitlelabel')
        self.subtitlelabel.setGeometry(QtCore.QRect(40, 220, 300, 30))
        self.subtitlelabel.setStyleSheet('#subtitlelabel{\n    color:#6b7280;\n    background:transparent;\n    font-size:13px;\n}')
        self.subtitlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loginbutton = QtWidgets.QPushButton(self.completeframe)
        self.loginbutton.setObjectName('loginbutton')
        self.loginbutton.setGeometry(QtCore.QRect(40, 300, 300, 45))
        self.loginbutton.setStyleSheet('#loginbutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:8px;\n    font-weight:bold;\n}')

        self.retranslateui(signup_complete)
        QtCore.QMetaObject.connectSlotsByName(signup_complete)

    def retranslateui(self, signup_complete):
        _translate = QtCore.QCoreApplication.translate
        signup_complete.setWindowTitle(_translate('signup_complete_page', 'Form'))
        self.checklabel.setText(_translate('signup_complete_page', '체크 이미지 넣기'))
        self.titlelabel.setText(_translate('signup_complete_page', '회원가입 완료'))
        self.subtitlelabel.setText(_translate('signup_complete_page', '로그인 후 서비스를 이용해주세요.'))
        self.loginbutton.setText(_translate('signup_complete_page', '로그인 화면으로 이동'))
