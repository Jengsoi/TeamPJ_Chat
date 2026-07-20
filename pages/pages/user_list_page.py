# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_list_page.ui'
##
## Created by: ChatGPT UI converter for PySide6
##
## WARNING! All changes made in this file may be lost if regenerated!
################################################################################

from PySide6 import QtCore,QtGui, QtWidgets


class Ui_user_list(object):
    def setupUi(self, user_list):
        if not user_list.objectName():
            user_list.setObjectName('user_list')
        user_list.resize(500, 660)
        user_list.setStyleSheet('#userlistframe{\n    background:#f8fafc;\n    border:none;\n}')
        self.onlinelabel = QtWidgets.QLabel(user_list)
        self.onlinelabel.setObjectName('onlinelabel')
        self.onlinelabel.setGeometry(QtCore.QRect(20, 20, 200, 25))
        self.onlinelabel.setStyleSheet('#onlinelabel{\n    background:transparent;\n    color:#111827;\n    font-size:15px;\n    font-weight:bold;\n}')
        self.userlistwidget = QtWidgets.QListWidget(user_list)
        self.userlistwidget.setObjectName('userlistwidget')
        self.userlistwidget.setGeometry(QtCore.QRect(25, 50, 460, 560))
        self.userlistwidget.setStyleSheet('#userlistwidget{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n    padding:6px;\n    color:#111827;\n}\n\n#userlistwidget::item{\n    height:52px;\n    padding-left:10px;\n    border-bottom:1px solid #f3f4f6;\n}\n\n#userlistwidget::item:selected{\n    background:#dbeafe;\n    color:#1d4ed8;\n    border-radius:8px;\n}')
        self.userlistwidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.retranslateUi(user_list)
        QtCore.QMetaObject.connectSlotsByName(user_list)

    def retranslateUi(self, user_list):
        _translate = QtCore.QCoreApplication.translate
        user_list.setWindowTitle(_translate('userlistframe', 'Form'))
        self.onlinelabel.setText(_translate('userlistframe', '사용자 list'))
