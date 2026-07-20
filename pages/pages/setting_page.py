# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_setting(object):
    def setupUi(self, setting):
        if not setting.objectName():
            setting.setObjectName('setting_page')
        setting.resize(500, 660)
        self.settingframe = QtWidgets.QFrame(setting)
        self.settingframe.setObjectName('settingframe')
        self.settingframe.setGeometry(QtCore.QRect(0, 0, 500, 660))
        self.settingframe.setStyleSheet('#settingframe{\n    background:#f8fafc;\n    border:none;\n}')
        self.settingframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settingframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.profilebutton = QtWidgets.QPushButton(self.settingframe)
        self.profilebutton.setObjectName('profilebutton')
        self.profilebutton.setGeometry(QtCore.QRect(20, 30, 460, 55))
        self.profilebutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')
        self.accountbutton = QtWidgets.QPushButton(self.settingframe)
        self.accountbutton.setObjectName('accountbutton')
        self.accountbutton.setGeometry(QtCore.QRect(20, 110, 460, 55))
        self.accountbutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')
        self.notificationbutton = QtWidgets.QPushButton(self.settingframe)
        self.notificationbutton.setObjectName('notificationbutton')
        self.notificationbutton.setGeometry(QtCore.QRect(20, 190, 460, 55))
        self.notificationbutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')
        self.chatsettingbutton = QtWidgets.QPushButton(self.settingframe)
        self.chatsettingbutton.setObjectName('chatsettingbutton')
        self.chatsettingbutton.setGeometry(QtCore.QRect(20, 270, 460, 55))
        self.chatsettingbutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')
        self.filemanagebutton = QtWidgets.QPushButton(self.settingframe)
        self.filemanagebutton.setObjectName('filemanagebutton')
        self.filemanagebutton.setGeometry(QtCore.QRect(20, 350, 460, 55))
        self.filemanagebutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')
        self.logoutbutton = QtWidgets.QPushButton(self.settingframe)
        self.logoutbutton.setObjectName('logoutbutton')
        self.logoutbutton.setGeometry(QtCore.QRect(20, 430, 460, 55))
        self.logoutbutton.setStyleSheet('QPushButton{\n    background:#ffffff;\n    color:#111827;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    font-size:14px;\n    text-align:left;\n    padding-left:18px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}')

        self.retranslateui(setting)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateui(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate('setting_page', 'Form'))
        self.profilebutton.setText(_translate('setting_page', '프로필 관리'))
        self.accountbutton.setText(_translate('setting_page', '계정 관리'))
        self.notificationbutton.setText(_translate('setting_page', '알림 설정'))
        self.chatsettingbutton.setText(_translate('setting_page', '채팅 설정'))
        self.filemanagebutton.setText(_translate('setting_page', '파일 / 이미지 관리'))
        self.logoutbutton.setText(_translate('setting_page', '로그아웃'))
