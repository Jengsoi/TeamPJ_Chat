# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attach_dialog.ui'
## Generated for PySide6 by fallback converter.
################################################################################

from PySide6 import QtCore, QtWidgets


class Ui_attach_dialog(object):
    def setupUi(self, attach_dialog):
        attach_dialog.setObjectName('attach_dialog')
        attach_dialog.resize(300, 320)
        attach_dialog.setWindowTitle('Dialog')
        self.attachframe = QtWidgets.QFrame(attach_dialog)
        self.attachframe.setObjectName('attachframe')
        self.attachframe.setGeometry(QtCore.QRect(0, 0, 300, 320))
        self.attachframe.setStyleSheet('#attachframe{\n    background:#ffffff;\n    border:1px solid #e5e7eb;\n    border-radius:12px;\n}')
        self.attachframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.attachframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlelabel = QtWidgets.QLabel(self.attachframe)
        self.titlelabel.setObjectName('titlelabel')
        self.titlelabel.setGeometry(QtCore.QRect(30, 20, 240, 30))
        self.titlelabel.setStyleSheet('#titlelabel{\n    background:transparent;\n    color:#111827;\n    font-size:18px;\n    font-weight:bold;\n}')
        self.titlelabel.setText('첨부하기')
        self.titlelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imagebutton = QtWidgets.QPushButton(self.attachframe)
        self.imagebutton.setObjectName('imagebutton')
        self.imagebutton.setGeometry(QtCore.QRect(30, 70, 240, 45))
        self.imagebutton.setStyleSheet('#imagebutton{\n    background:#f8fafc;\n    color:#111827;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    font-size:14px;\n}')
        self.imagebutton.setText('🖼 이미지 첨부')
        self.filebutton = QtWidgets.QPushButton(self.attachframe)
        self.filebutton.setObjectName('filebutton')
        self.filebutton.setGeometry(QtCore.QRect(30, 125, 240, 45))
        self.filebutton.setStyleSheet('#filebutton{\n    background:#f8fafc;\n    color:#111827;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    font-size:14px;\n}')
        self.filebutton.setText('📁 파일 첨부')
        self.schedulebutton = QtWidgets.QPushButton(self.attachframe)
        self.schedulebutton.setObjectName('schedulebutton')
        self.schedulebutton.setGeometry(QtCore.QRect(30, 180, 240, 45))
        self.schedulebutton.setStyleSheet('#schedulebutton{\n    background:#f8fafc;\n    color:#111827;\n    border:1px solid #d1d5db;\n    border-radius:8px;\n    font-size:14px;\n}')
        self.schedulebutton.setText('📅 일정 보내기')
        self.cancelbutton = QtWidgets.QPushButton(self.attachframe)
        self.cancelbutton.setObjectName('cancelbutton')
        self.cancelbutton.setGeometry(QtCore.QRect(30, 250, 240, 42))
        self.cancelbutton.setStyleSheet('#cancelbutton{\n    background:#ffffff;\n    color:#6b7280;\n    border:none;\n    font-size:13px;\n}')
        self.cancelbutton.setText('취소하기')

        self.retranslateui(attach_dialog)
        QtCore.QMetaObject.connectSlotsByName(attach_dialog)

    def retranslateui(self, attach_dialog):
        pass
