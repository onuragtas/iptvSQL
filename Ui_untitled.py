# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/onuragtas/Workspace/iptv2/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(704, 402)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.selectButton = QtWidgets.QPushButton(Dialog)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 0, 0, 1, 1)
        self.m3uText = QtWidgets.QPlainTextEdit(Dialog)
        self.m3uText.setObjectName("m3uText")
        self.gridLayout.addWidget(self.m3uText, 1, 0, 1, 1)
        self.sqlText = QtWidgets.QPlainTextEdit(Dialog)
        self.sqlText.setObjectName("sqlText")
        self.gridLayout.addWidget(self.sqlText, 2, 0, 1, 1)
        self.sqlButton = QtWidgets.QPushButton(Dialog)
        self.sqlButton.setObjectName("sqlButton")
        self.gridLayout.addWidget(self.sqlButton, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.selectButton.setText(_translate("Dialog", "Select M3U File"))
        self.sqlButton.setText(_translate("Dialog", "Get SQL"))

