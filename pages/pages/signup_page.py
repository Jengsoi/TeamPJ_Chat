# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_signup(object):
    def setupUi(self, signup):
        if not signup.objectName():
            signup.setObjectName('signup')
        signup.resize(500, 800)
        signup.setStyleSheet('background:#f8fafc;')
        self.signupframe = QtWidgets.QFrame(signup)
        self.signupframe.setObjectName('signupframe')
        self.signupframe.setGeometry(QtCore.QRect(60, 80, 380, 610))
        self.signupframe.setStyleSheet('#signupframe{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n}')
        self.signupframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.signupframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.signupframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(135, 20, 110, 25))
        self.titlelabel.setStyleSheet('#titlelabel{\n    color:#2563eb;\n    background:transparent;\n    font-size:22px;\n    font-weight:bold;\n}')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.employeeinput = QtWidgets.QLineEdit(self.signupframe)
        self.employeeinput.setObjectName('employeeinput')
        self.employeeinput.setGeometry(QtCore.QRect(30, 80, 320, 38))
        self.employeeinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.employeeinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nameinput = QtWidgets.QLineEdit(self.signupframe)
        self.nameinput.setObjectName('nameinput')
        self.nameinput.setGeometry(QtCore.QRect(30, 130, 320, 38))
        self.nameinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.nameinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.phoneinput = QtWidgets.QLineEdit(self.signupframe)
        self.phoneinput.setObjectName('phoneinput')
        self.phoneinput.setGeometry(QtCore.QRect(30, 180, 320, 38))
        self.phoneinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.phoneinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.idinput = QtWidgets.QLineEdit(self.signupframe)
        self.idinput.setObjectName('idinput')
        self.idinput.setGeometry(QtCore.QRect(30, 230, 320, 38))
        self.idinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.idinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pwinput = QtWidgets.QLineEdit(self.signupframe)
        self.pwinput.setObjectName('pwinput')
        self.pwinput.setGeometry(QtCore.QRect(30, 280, 320, 38))
        self.pwinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.pwinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nicknameinput = QtWidgets.QLineEdit(self.signupframe)
        self.nicknameinput.setObjectName('nicknameinput')
        self.nicknameinput.setGeometry(QtCore.QRect(30, 330, 320, 38))
        self.nicknameinput.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.nicknameinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signupbutton = QtWidgets.QPushButton(self.signupframe)
        self.signupbutton.setObjectName('signupbutton')
        self.signupbutton.setGeometry(QtCore.QRect(30, 450, 320, 42))
        self.signupbutton.setStyleSheet('#signupbutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:6px;\n    font-weight:bold;\n}')
        self.pushButton = QtWidgets.QPushButton(self.signupframe)
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setGeometry(QtCore.QRect(15, 15, 28, 28))
        self.pushButton.setStyleSheet('#backbutton{\n    background:transparent;\n    border:none;\n}')
        self.backloginbutton = QtWidgets.QPushButton(self.signupframe)
        self.backloginbutton.setObjectName('backloginbutton')
        self.backloginbutton.setGeometry(QtCore.QRect(30, 500, 320, 30))
        self.backloginbutton.setStyleSheet('#backloginbutton{\n    background:transparent;\n    border:none;\n    color:#2563eb;\n    font-size:12px;\n    font-weight:600;\n}\n\n#backloginbutton{\n    background:transparent;\n    border:none;\n    color:#2563eb;\n    font-size:12px;\n    font-weight:600;\n}\n\n#backloginbutton:hover{\n    color:#1d4ed8;\n    text-decoration: underline;\n}\n\n#backloginbutton:pressed{\n    color:#1e40af;\n}')
        self.nicknameinput_2 = QtWidgets.QLineEdit(self.signupframe)
        self.nicknameinput_2.setObjectName('nicknameinput_2')
        self.nicknameinput_2.setGeometry(QtCore.QRect(30, 380, 320, 38))
        self.nicknameinput_2.setStyleSheet('  background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:6px;\n    padding-left:10px;\n')
        self.nicknameinput_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate('Form', 'Form'))
        self.titlelabel.setText(_translate('Form', '회원가입'))
        self.signupbutton.setText(_translate('Form', '회원가입'))
        self.pushButton.setText(_translate('Form', '<'))
        self.backloginbutton.setText(_translate('Form', '이미 계정이 있으신가요? 로그인으로 돌아가기'))
