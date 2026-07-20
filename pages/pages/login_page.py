# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName('Form')
        login.resize(500, 800)
        login.setStyleSheet('background:#F8FAFC;')
        self.loginframe = QtWidgets.QFrame(login)
        self.loginframe.setObjectName('loginframe')
        self.loginframe.setGeometry(QtCore.QRect(60, 120, 380, 520))
        self.loginframe.setStyleSheet('#loginframe {\n    background:#FFFFFF;\n    border:1px solid #E5E7EB;\n    border-radius:16px;\n}')
        self.loginframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loginframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.loginframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(65, 45, 250, 50))
        self.titlelabel.setStyleSheet('color:#2563EB;\nfont-size:26px;\nfont-weight:bold;\nbackground:transparent;')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subtitlelabel = QtWidgets.QLabel(self.loginframe)
        self.subtitlelabel.setObjectName('subtitlelabel')
        self.subtitlelabel.setGeometry(QtCore.QRect(90, 95, 200, 30))
        self.subtitlelabel.setStyleSheet('color:#6B7280;\nfont-size:13px;\nbackground:transparent;')
        self.subtitlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.idinput = QtWidgets.QLineEdit(self.loginframe)
        self.idinput.setObjectName('idinput')
        self.idinput.setGeometry(QtCore.QRect(40, 170, 300, 45))
        self.idinput.setStyleSheet('#idinput, #pwinput {\nbackground:#FFFFFF;\nborder:1px solid #D1D5DB;\nborder-radius:8px;\npadding-left:10px;}')
        self.pwinput = QtWidgets.QLineEdit(self.loginframe)
        self.pwinput.setObjectName('pwinput')
        self.pwinput.setGeometry(QtCore.QRect(40, 230, 300, 45))
        self.pwinput.setStyleSheet('#idinput, #pwinput {\nbackground:#FFFFFF;\nborder:1px solid #D1D5DB;\nborder-radius:8px;\npadding-left:10px;}')
        self.pwinput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.loginbutton = QtWidgets.QPushButton(self.loginframe)
        self.loginbutton.setObjectName('loginbutton')
        self.loginbutton.setGeometry(QtCore.QRect(40, 310, 300, 45))
        self.loginbutton.setStyleSheet('background-color:#2563EB;\ncolor:#FFFFFF;\nborder:none;\nborder-radius:8px;\nfont-weight:bold;')
        self.signupbutton = QtWidgets.QPushButton(self.loginframe)
        self.signupbutton.setObjectName('signupbutton')
        self.signupbutton.setGeometry(QtCore.QRect(40, 370, 300, 45))
        self.signupbutton.setStyleSheet('#signupbutton\n{background:#FFFFFF;\ncolor:#2563EB;\nborder:1px solid #2563EB;\nborder-radius:8px;\nfont-weight:bold;}')

        self.retranslateui(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateui(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate('Form', 'Form'))
        self.titlelabel.setText(_translate('Form', 'CodeLink'))
        self.subtitlelabel.setText(_translate('Form', '개발자 협업 메신저'))
        self.loginbutton.setText(_translate('Form', '로그인'))
        self.signupbutton.setText(_translate('Form', '회원가입'))
