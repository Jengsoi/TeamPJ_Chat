# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_list_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_chat_list(object):
    def setupUi(self, chat_list):
        if not chat_list.objectName():
            chat_list.setObjectName('chat_list_page')
        chat_list.resize(500, 660)
        self.chatlistframe = QtWidgets.QFrame(chat_list)
        self.chatlistframe.setObjectName('chatlistframe')
        self.chatlistframe.setGeometry(QtCore.QRect(0, 0, 500, 660))
        self.chatlistframe.setStyleSheet('#chatlistframe{\n    background:#f8fafc;\n    border:none;\n}')
        self.chatlistframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.chatlistframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.chatlistwidget = QtWidgets.QListWidget(self.chatlistframe)
        self.chatlistwidget.setObjectName('chatlistwidget')
        self.chatlistwidget.setGeometry(QtCore.QRect(20, 80, 460, 560))
        self.chatlistwidget.setStyleSheet('#chatlistwidget{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    outline:none;\n}\n\n#chatlistwidget::item{\n    height:70px;\n    padding-left:15px;\n}\n\n#chatlistwidget::item:hover{\n    background:#f3f4f6;\n}\n\n#chatlistwidget::item:selected{\n    background:#dbeafe;\n    color:#2563eb;\n}')
        self.chatlistwidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.addroombutton = QtWidgets.QLabel(self.chatlistframe)
        self.addroombutton.setObjectName('addroombutton')
        self.addroombutton.setGeometry(QtCore.QRect(415, 20, 45, 45))
        self.addroombutton.setStyleSheet('#addroombutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:15px;\n    font-size:18px;\n    font-weight:bold;\n}\n\n#addroombutton:hover{\n    background:#1d4ed8;\n}\n\n#addroombutton:pressed{\n    background:#1e40af;\n}')
        self.addroombutton.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateui(chat_list)
        QtCore.QMetaObject.connectSlotsByName(chat_list)

    def retranslateui(self, chat_list):
        _translate = QtCore.QCoreApplication.translate
        chat_list.setWindowTitle(_translate('chat_list_page', 'Form'))
        self.addroombutton.setText(_translate('chat_list_page', '+'))
