# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGameAsk.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewGameAsk(object):
    def setupUi(self, NewGameAsk):
        NewGameAsk.setObjectName("NewGameAsk")
        NewGameAsk.setEnabled(True)
        NewGameAsk.resize(284, 123)
        self.label = QtWidgets.QLabel(NewGameAsk)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.newGameYeasBtn = QtWidgets.QPushButton(NewGameAsk)
        self.newGameYeasBtn.setGeometry(QtCore.QRect(30, 70, 75, 23))
        self.newGameYeasBtn.setObjectName("newGameYeasBtn")
        self.newGameNoBtn = QtWidgets.QPushButton(NewGameAsk)
        self.newGameNoBtn.setGeometry(QtCore.QRect(170, 70, 75, 23))
        self.newGameNoBtn.setObjectName("newGameNoBtn")

        self.retranslateUi(NewGameAsk)
        QtCore.QMetaObject.connectSlotsByName(NewGameAsk)

    def retranslateUi(self, NewGameAsk):
        _translate = QtCore.QCoreApplication.translate
        NewGameAsk.setWindowTitle(_translate("NewGameAsk", "Form"))
        self.label.setText(_translate("NewGameAsk", "вы хотите начать новую игру?"))
        self.newGameYeasBtn.setText(_translate("NewGameAsk", "да"))
        self.newGameNoBtn.setText(_translate("NewGameAsk", "нет"))
