# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsAction.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def savesettings(self):
        self.host = self.hostName.text()
        self.port = self.portNumber.text()
        self.username = self.senderEmail.text()
        self.passWWord = self.password.text()
        self.show_popup('Message', 'Properties saved successfully!', QMessageBox.Information)

    def show_popup(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 240)
        Dialog.setStyleSheet("background-color: rgb(197,239,247);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(23, 34, 54, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(15, 63, 62, 13))
        self.label_2.setObjectName("label_2")
        self.hostName = QtWidgets.QLineEdit(Dialog)
        self.hostName.setGeometry(QtCore.QRect(90, 30, 281, 20))
        self.hostName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hostName.setObjectName("hostName")
        self.portNumber = QtWidgets.QLineEdit(Dialog)
        self.portNumber.setGeometry(QtCore.QRect(90, 60, 281, 20))
        self.portNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.portNumber.setObjectName("portNumber")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(52, 94, 26, 13))
        self.label_4.setObjectName("label_4")
        self.senderEmail = QtWidgets.QLineEdit(Dialog)
        self.senderEmail.setGeometry(QtCore.QRect(90, 90, 281, 20))
        self.senderEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senderEmail.setObjectName("senderEmail")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(31, 125, 48, 13))
        self.label_5.setObjectName("label_5")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(90, 122, 281, 20))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(170, 170, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.save.setObjectName("save")
        ##################### save settings #########################
        self.save.clicked.connect(self.savesettings)
        #############################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "Host Name:"))
        self.label_2.setText(_translate("Dialog", "Port Number:"))

        self.label_4.setText(_translate("Dialog", "Email:"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.save.setText(_translate("Dialog", "SAVE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
