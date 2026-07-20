# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName('개발자메신저')
        main.resize(800, 1000)
        self.mainframe = QtWidgets.QFrame(main)
        self.mainframe.setObjectName('mainframe')
        self.mainframe.setGeometry(QtCore.QRect(500, 800, 120, 80))
        self.mainframe.setStyleSheet('#mainframe{\n    background:#f8fafc;\n}')
        self.mainframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headerframe = QtWidgets.QFrame(main)
        self.headerframe.setObjectName('headerframe')
        self.headerframe.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.headerframe.setStyleSheet('#headerframe{\n    background:#ffffff;\n    border:none;\n    border-bottom:1px solid #e5e7eb;\n}')
        self.headerframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.headerframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.contentframe = QtWidgets.QFrame(main)
        self.contentframe.setObjectName('contentframe')
        self.contentframe.setGeometry(QtCore.QRect(0, 70, 500, 660))
        self.contentframe.setStyleSheet('#contentframe{\n    background:#f8fafc;\n    border:none;\n}')
        self.contentframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.contentframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.stackedWidget = QtWidgets.QStackedWidget(self.contentframe)
        self.stackedWidget.setObjectName('stackedWidget')
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 500, 660))
        self.stackedWidget.setStyleSheet('#contentstack{\n    background:#f8fafc;\n    border:none;\n}')
        self.page_3 = QtWidgets.QWidget(self.stackedWidget)
        self.page_3.setObjectName('page_3')
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget(self.stackedWidget)
        self.page_4.setObjectName('page_4')
        self.stackedWidget.addWidget(self.page_4)
        self.bottomframe = QtWidgets.QFrame(main)
        self.bottomframe.setObjectName('bottomframe')
        self.bottomframe.setGeometry(QtCore.QRect(0, 730, 500, 70))
        self.bottomframe.setStyleSheet('#bottomframe{\n    background:#ffffff;\n    border:none;\n    border-top:1px solid #e5e7eb;\n}')
        self.bottomframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.userbutton = QtWidgets.QPushButton(self.bottomframe)
        self.userbutton.setObjectName('userbutton')
        self.userbutton.setGeometry(QtCore.QRect(0, 0, 166, 70))
        self.userbutton.setStyleSheet('QPushButton{\n    background:transparent;\n    border:none;\n    color:#6b7280;\n    font-size:13px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}\n\nQPushButton:checked{\n    color:#2563eb;\n    font-weight:bold;\n}')
        self.chatbutton = QtWidgets.QPushButton(self.bottomframe)
        self.chatbutton.setObjectName('chatbutton')
        self.chatbutton.setGeometry(QtCore.QRect(167, 0, 166, 70))
        self.chatbutton.setStyleSheet('QPushButton{\n    background:transparent;\n    border:none;\n    color:#6b7280;\n    font-size:13px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}\n\nQPushButton:checked{\n    color:#2563eb;\n    font-weight:bold;\n}')
        self.settingbutton = QtWidgets.QPushButton(self.bottomframe)
        self.settingbutton.setObjectName('settingbutton')
        self.settingbutton.setGeometry(QtCore.QRect(334, 0, 166, 70))
        self.settingbutton.setStyleSheet('QPushButton{\n    background:transparent;\n    border:none;\n    color:#6b7280;\n    font-size:13px;\n}\n\nQPushButton:hover{\n    background:#f3f4f6;\n}\n\nQPushButton:pressed{\n    background:#e5e7eb;\n}\n\nQPushButton:checked{\n    color:#2563eb;\n    font-weight:bold;\n}')

        self.retranslateui(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateui(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate('mainwindow', 'Form'))
        self.userbutton.setText(_translate('mainwindow', '사용자 목록'))
        self.chatbutton.setText(_translate('mainwindow', '채팅'))
        self.settingbutton.setText(_translate('mainwindow', '설정'))
