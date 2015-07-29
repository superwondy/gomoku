# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created: Fri Feb 21 19:18:50 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginWidget(object):
    def setupUi(self, loginWidget):
        loginWidget.setObjectName(_fromUtf8("loginWidget"))
        loginWidget.resize(400, 217)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icon/unplay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWidget.setWindowIcon(icon)
        loginWidget.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-image: url(:/image/image/bg3.jpg);\n"
"    width: 500px;\n"
"}\n"
"\n"
"QPushButton,QLabel,QLineEdit{\n"
"    background-image: url();\n"
"}\n"
"\n"
"QPushButton#btClose{\n"
"    image: url(:/icon/icon/close.png);\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QLabel#labelNotice{\n"
"    font: 75 16pt \"Adobe 宋体 Std L\";\n"
"    color: rgb(255, 0, 0);\n"
"}"))
        self.label = QtGui.QLabel(loginWidget)
        self.label.setGeometry(QtCore.QRect(53, 60, 61, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.labelPass = QtGui.QLabel(loginWidget)
        self.labelPass.setGeometry(QtCore.QRect(53, 100, 61, 20))
        self.labelPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPass.setObjectName(_fromUtf8("labelPass"))
        self.lineEditIp = QtGui.QLineEdit(loginWidget)
        self.lineEditIp.setGeometry(QtCore.QRect(130, 60, 191, 20))
        self.lineEditIp.setObjectName(_fromUtf8("lineEditIp"))
        self.lineEditPort = QtGui.QLineEdit(loginWidget)
        self.lineEditPort.setGeometry(QtCore.QRect(130, 100, 191, 20))
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.btLogin = QtGui.QPushButton(loginWidget)
        self.btLogin.setGeometry(QtCore.QRect(170, 180, 91, 31))
        self.btLogin.setAutoDefault(True)
        self.btLogin.setObjectName(_fromUtf8("btLogin"))
        self.labelRigister = QtGui.QLabel(loginWidget)
        self.labelRigister.setGeometry(QtCore.QRect(340, 190, 61, 21))
        self.labelRigister.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRigister.setObjectName(_fromUtf8("labelRigister"))
        self.lineEditName = QtGui.QLineEdit(loginWidget)
        self.lineEditName.setGeometry(QtCore.QRect(127, 140, 191, 20))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.labelName = QtGui.QLabel(loginWidget)
        self.labelName.setGeometry(QtCore.QRect(50, 140, 61, 20))
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.labelNotice = QtGui.QLabel(loginWidget)
        self.labelNotice.setGeometry(QtCore.QRect(40, 30, 321, 20))
        self.labelNotice.setText(_fromUtf8(""))
        self.labelNotice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNotice.setObjectName(_fromUtf8("labelNotice"))
        self.btClose = QtGui.QPushButton(loginWidget)
        self.btClose.setGeometry(QtCore.QRect(369, 0, 31, 31))
        self.btClose.setText(_fromUtf8(""))
        self.btClose.setObjectName(_fromUtf8("btClose"))

        self.retranslateUi(loginWidget)
        QtCore.QMetaObject.connectSlotsByName(loginWidget)

    def retranslateUi(self, loginWidget):
        loginWidget.setWindowTitle(_translate("loginWidget", "登录", None))
        self.label.setText(_translate("loginWidget", "IP地址:", None))
        self.labelPass.setText(_translate("loginWidget", "端口号:", None))
        self.lineEditIp.setText(_translate("loginWidget", "127.0.0.1", None))
        self.lineEditPort.setText(_translate("loginWidget", "8888", None))
        self.btLogin.setText(_translate("loginWidget", "登录", None))
        self.labelRigister.setText(_translate("loginWidget", "注册", None))
        self.lineEditName.setText(_translate("loginWidget", "user", None))
        self.labelName.setText(_translate("loginWidget", "用户名:", None))

import login_rc
