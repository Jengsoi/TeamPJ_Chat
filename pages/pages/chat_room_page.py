# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_room_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_chat_room(object):
    def setupUi(self, chat_room):
        if not chat_room.objectName():
            chat_room.setObjectName('chat_room_page')
        chat_room.resize(500, 800)
        self.chatroomframe = QtWidgets.QFrame(chat_room)
        self.chatroomframe.setObjectName('chatroomframe')
        self.chatroomframe.setGeometry(QtCore.QRect(0, 0, 500, 800))
        self.chatroomframe.setStyleSheet('#chatroomframe{\n    background:#f8fafc;\n}')
        self.chatroomframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.chatroomframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headerframe = QtWidgets.QFrame(self.chatroomframe)
        self.headerframe.setObjectName('headerframe')
        self.headerframe.setGeometry(QtCore.QRect(0, 0, 500, 60))
        self.headerframe.setStyleSheet('#headerframe{\n    background:#ffffff;\n    border:none;\n    border-bottom:1px solid #e5e7eb;\n}')
        self.headerframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.headerframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.backbutton = QtWidgets.QPushButton(self.headerframe)
        self.backbutton.setObjectName('backbutton')
        self.backbutton.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.backbutton.setStyleSheet('#backbutton{\n    background:transparent;\n    border:none;\n    font-size:18px;\n}')
        self.roomtitlelabel = QtWidgets.QLabel(self.headerframe)
        self.roomtitlelabel.setObjectName('roomtitlelabel')
        self.roomtitlelabel.setGeometry(QtCore.QRect(60, 15, 380, 30))
        self.roomtitlelabel.setStyleSheet('#roomtitlelabel{\n    background:transparent;\n    font-size:18px;\n    font-weight:bold;\n}')
        self.roomtitlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.messageframe = QtWidgets.QFrame(self.chatroomframe)
        self.messageframe.setObjectName('messageframe')
        self.messageframe.setGeometry(QtCore.QRect(0, 60, 500, 660))
        self.messageframe.setStyleSheet('#messageframe{\n    background:#f8fafc;\n    border:none;\n}')
        self.messageframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.messageframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messagescrollarea = QtWidgets.QScrollArea(self.messageframe)
        self.messagescrollarea.setObjectName('messagescrollarea')
        self.messagescrollarea.setGeometry(QtCore.QRect(0, 0, 500, 660))
        self.messagescrollarea.setStyleSheet('#messagescrollarea{\n    background:#f8fafc;\n    border:none;\n}')
        self.messagescrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.messagescrollarea)
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContents')
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 660))
        self.messagescrollarea.setWidget(self.scrollAreaWidgetContents)
        self.inputframe = QtWidgets.QFrame(self.chatroomframe)
        self.inputframe.setObjectName('inputframe')
        self.inputframe.setGeometry(QtCore.QRect(0, 720, 500, 80))
        self.inputframe.setStyleSheet('#inputframe{\n    background:#ffffff;\n    border-top:1px solid #e5e7eb;\n}')
        self.inputframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.inputframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.attachbutton = QtWidgets.QPushButton(self.inputframe)
        self.attachbutton.setObjectName('attachbutton')
        self.attachbutton.setGeometry(QtCore.QRect(10, 20, 40, 40))
        self.attachbutton.setStyleSheet('#attachbutton{\n    background:transparent;\n    border:none;\n    font-size:22px;\n}')
        self.messageinput = QtWidgets.QLineEdit(self.inputframe)
        self.messageinput.setObjectName('messageinput')
        self.messageinput.setGeometry(QtCore.QRect(60, 20, 340, 40))
        self.messageinput.setStyleSheet('#messageinput{\n    background:#ffffff;\n    border:1px solid #d1d5db;\n    border-radius:18px;\n    padding-left:15px;\n}')
        self.sendbutton = QtWidgets.QPushButton(self.inputframe)
        self.sendbutton.setObjectName('sendbutton')
        self.sendbutton.setGeometry(QtCore.QRect(410, 20, 75, 40))
        self.sendbutton.setStyleSheet('#sendbutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:18px;\n    font-weight:bold;\n}')

        self.retranslateui(chat_room)
        QtCore.QMetaObject.connectSlotsByName(chat_room)

    def retranslateui(self, chat_room):
        _translate = QtCore.QCoreApplication.translate
        chat_room.setWindowTitle(_translate('chat_room_page', 'Form'))
        self.backbutton.setText(_translate('chat_room_page', '←'))
        self.roomtitlelabel.setText(_translate('chat_room_page', 'roomtitlelabel'))
        self.attachbutton.setText(_translate('chat_room_page', '+'))
        self.sendbutton.setText(_translate('chat_room_page', '전송'))
