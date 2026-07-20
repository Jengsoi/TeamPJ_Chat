# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_chat_dialog.ui'
## Generated for PySide6 by fallback converter.
################################################################################

from PySide6 import QtCore, QtWidgets


class Ui_create_chat_dialog(object):
    def setupUi(self, createchatdialog):
        createchatdialog.setObjectName('createchatdialog')
        createchatdialog.resize(360, 520)
        createchatdialog.setWindowTitle('Dialog')
        self.createchatframe = QtWidgets.QFrame(createchatdialog)
        self.createchatframe.setObjectName('createchatframe')
        self.createchatframe.setGeometry(QtCore.QRect(0, 0, 360, 520))
        self.createchatframe.setStyleSheet('#createchatframe{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n}')
        self.createchatframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.createchatframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.createchatframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(30, 20, 300, 30))
        self.titlelabel.setStyleSheet('#titlelabel{\n    background:transparent;\n    color:#111827;\n    font-size:17px;\n    font-weight:bold;\n}')
        self.titlelabel.setText('채팅할 사용자 선택')
        self.userlistwidget = QtWidgets.QListWidget(self.createchatframe)
        self.userlistwidget.setObjectName('userlistwidget')
        self.userlistwidget.setGeometry(QtCore.QRect(30, 70, 300, 330))
        self.userlistwidget.setStyleSheet('#userlistwidget{\n    background:#f8fafc;\n    border:1px solid #e5e7eb;\n    border-radius:10px;\n    outline:none;\n}\n\n#userlistwidget::item{\n    height:45px;\n    padding-left:10px;\n}\n\n#userlistwidget::item:selected{\n    background:#dbeafe;\n    color:#2563eb;\n}')
        self.userlistwidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.userlistwidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.createbutton = QtWidgets.QPushButton(self.createchatframe)
        self.createbutton.setObjectName('createbutton')
        self.createbutton.setGeometry(QtCore.QRect(30, 410, 300, 40))
        self.createbutton.setStyleSheet('#createbutton{\n    background:#2563eb;\n    color:#ffffff;\n    border:none;\n    border-radius:8px;\n    font-weight:bold;\n}')
        self.createbutton.setText('채팅 시작')
        self.cancelbutton = QtWidgets.QPushButton(self.createchatframe)
        self.cancelbutton.setObjectName('cancelbutton')
        self.cancelbutton.setGeometry(QtCore.QRect(30, 460, 300, 40))
        self.cancelbutton.setStyleSheet('#cancelbutton{\n    background:transparent;\n    color:#6b7280;\n    border:none;\n}')
        self.cancelbutton.setText('취소')

        self.retranslateui(createchatdialog)
        QtCore.QMetaObject.connectSlotsByName(createchatdialog)

    def retranslateui(self, createchatdialog):
        pass
