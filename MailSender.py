# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import csv
import mimetypes
import os
import smtplib
import sys

try:
    from smtplib import SMTP, SMTP_SSL, SMTPException, SMTPSenderRefused, SMTPHeloError, \
        SMTPNotSupportedError, SMTPAuthenticationError, SMTPRecipientsRefused, SMTPDataError, SMTPServerDisconnected, \
        SMTPConnectError
except:
    sys.exit("Sorry, requires Version 3.x")

from email.header import Header
from email.utils import formatdate, formataddr, COMMASPACE
from email.message import EmailMessage

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from ActionSettings import Ui_Dialog


class Ui_MainWindow(object):
    def __init__(self):
        self.attachment_path = None

    def settingsCheck(self):
        self.settingwindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.settingwindow)
        self.settingwindow.show()
        self.ui.save.clicked.connect(self.first)

    def first(self):
        self.settingwindow.close()

    def openFileDialogForEmail(self):
        try:
            filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open', 'C://', 'CSV files (*.csv)')
            self.email_path = filename[0]
            email_file = self.email_path.split("/")[-1]
            self.receiversEmail.setText(email_file)

        except:
            self.show_popup1('Warning', 'Invalid file type, select a .csv file', QMessageBox.Warning)
            self.receiversEmail.clear()

    def openFileDialogForAttachment(self):
        try:
            filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open', 'C://', 'All Files (*)')
            self.attachment_path = filename[0]
            attachment_file = self.attachment_path.split("/")[-1]
            self.attachmentPath.setText(attachment_file)

        except:
            self.show_popup1('Warning', 'Select a valid file', QMessageBox.Warning)
            self.attachmentPath.clear()

    def deleteAttachment(self):
        self.attachmentPath.clear()

    def sendMail(self):
        try:
            sender = self.senderName.text()

            with open(self.email_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)

                smtp = smtplib.SMTP(self.ui.host, self.ui.port)
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(self.ui.username, self.ui.passWWord)

                for row in csv_reader:
                    emaillist = row
                    if emaillist:
                        usern = emaillist[0].split('@')[0].capitalize()
                        fulldomain = emaillist[0].split('@')[1]
                        domainn = fulldomain.split('.')[0].capitalize()

                    email_msg = EmailMessage()
                    email_msg['From'] = formataddr((str(Header(sender, 'utf-8')), self.ui.username))
                    email_msg['To'] = COMMASPACE.join(emaillist)
                    email_msg['Subject'] = self.subject.text()
                    email_msg['Reply-To'] = self.ui.username
                    email_msg['Date'] = formatdate(localtime=True)
                    messagebody = self.message.toHtml().replace('usern', usern).replace('domainn', domainn) \
                        .replace('fulldomain', fulldomain)

                    if self.attachment_path is None:
                        email_msg.set_content(messagebody, subtype='html')

                    else:
                        email_msg.set_content(messagebody, subtype='html')
                        ctype, encoding = mimetypes.guess_type(self.attachment_path)
                        if ctype is None or encoding is not None:
                            # No guess could be made, or the file is encoded (compressed), so
                            # use a generic bag-of-bits type.
                            ctype = 'application/octet-stream'
                        maintype, subtype = ctype.split('/', 1)
                        filename = os.path.basename(self.attachment_path)
                        with open(self.attachment_path, 'rb') as fp:
                            email_msg.add_attachment(fp.read(),
                                                     maintype=maintype,
                                                     subtype=subtype,
                                                     filename=filename)

                    smtp.send_message(email_msg)

                    for x in emaillist:
                        a = 'Message successfully sent to ' + x
                    self.log.append(a)

                smtp.quit()

        except SMTPHeloError:
            self.log.setText('Server did not reply.')
        except SMTPNotSupportedError:
            self.log.setText("SMTP NOT SUPPORTED")
        except SMTPAuthenticationError:
            self.log.setText('Incorrect Username or Password.')
        except SMTPRecipientsRefused as e:
            self.log.setText(e)
        except SMTPException:
            self.log.setText('Authentication failed!')
        except SMTPConnectError:
            self.log.setText("Connection Error!")
        except SMTPDataError as e:
            self.log.setText(e)
        except FileNotFoundError:
            self.log.setText('File not found!')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 568)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(197,239,247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(10, 407, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.send.setObjectName("send")
        ################ send mail ################################
        self.send.clicked.connect(self.sendMail)
        ###########################################################
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_5.setObjectName("label_5")
        self.receiversEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.receiversEmail.setGeometry(QtCore.QRect(100, 20, 461, 20))
        self.receiversEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.receiversEmail.setDragEnabled(False)
        self.receiversEmail.setObjectName("receiversEmail")
        self.getEmailFile = QtWidgets.QPushButton(self.centralwidget)
        self.getEmailFile.setGeometry(QtCore.QRect(580, 20, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.getEmailFile.setFont(font)
        self.getEmailFile.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.getEmailFile.setObjectName("getEmailFile")
        ##########################################################################
        self.getEmailFile.clicked.connect(self.openFileDialogForEmail)
        ##########################################################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 41, 16))
        self.label.setObjectName("label")
        self.subject = QtWidgets.QLineEdit(self.centralwidget)
        self.subject.setGeometry(QtCore.QRect(100, 50, 461, 20))
        self.subject.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subject.setObjectName("subject")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 66, 20))
        self.label_4.setObjectName("label_4")
        self.senderName = QtWidgets.QLineEdit(self.centralwidget)
        self.senderName.setGeometry(QtCore.QRect(100, 80, 461, 20))
        self.senderName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senderName.setObjectName("senderName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.attachmentPath = QtWidgets.QLineEdit(self.centralwidget)
        self.attachmentPath.setGeometry(QtCore.QRect(100, 110, 381, 20))
        self.attachmentPath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.attachmentPath.setObjectName("attachmentPath")
        self.attachbutton = QtWidgets.QPushButton(self.centralwidget)
        self.attachbutton.setGeometry(QtCore.QRect(500, 110, 71, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.attachbutton.setFont(font)
        self.attachbutton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.attachbutton.setObjectName("attachbutton")
        ##########################################################################
        self.attachbutton.clicked.connect(self.openFileDialogForAttachment)
        ##########################################################################
        self.deleteAttachButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAttachButton.setEnabled(True)
        self.deleteAttachButton.setGeometry(QtCore.QRect(585, 110, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deleteAttachButton.setFont(font)
        self.deleteAttachButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.deleteAttachButton.setObjectName("deleteAttachButton")
        ##########################################################################
        self.deleteAttachButton.clicked.connect(self.deleteAttachment)
        ##########################################################################
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(100, 150, 561, 281))
        self.message.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.message.setObjectName("message")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(100, 460, 561, 41))
        self.log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.log.setObjectName("log")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 438, 31, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        ################## open settings ######################
        self.actionSettings.triggered.connect(self.settingsCheck)
        #######################################################
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email Sender"))
        self.send.setText(_translate("MainWindow", "SEND"))
        self.label_5.setText(_translate("MainWindow", "Reciever\'s Email:"))
        self.getEmailFile.setText(_translate("MainWindow", "Get Email File"))
        self.label.setText(_translate("MainWindow", "Subject:"))
        self.label_4.setText(_translate("MainWindow", "Sender Name:"))
        self.label_2.setText(_translate("MainWindow", "Attachment:"))
        self.attachbutton.setText(_translate("MainWindow", "Attach File"))
        self.deleteAttachButton.setText(_translate("MainWindow", "Delete File"))
        self.label_6.setText(_translate("MainWindow", "LOGS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

    def show_popup1(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
