# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\register.ui'
#
# Created: Fri Feb 21 19:18:51 2014
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

class Ui_registerWidget(object):
    def setupUi(self, registerWidget):
        registerWidget.setObjectName(_fromUtf8("registerWidget"))
        registerWidget.resize(400, 230)
        self.lineEditPass = QtGui.QLineEdit(registerWidget)
        self.lineEditPass.setGeometry(QtCore.QRect(130, 100, 191, 20))
        self.lineEditPass.setObjectName(_fromUtf8("lineEditPass"))
        self.labelPass = QtGui.QLabel(registerWidget)
        self.labelPass.setGeometry(QtCore.QRect(43, 100, 71, 20))
        self.labelPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPass.setObjectName(_fromUtf8("labelPass"))
        self.lineEditName = QtGui.QLineEdit(registerWidget)
        self.lineEditName.setGeometry(QtCore.QRect(130, 60, 191, 20))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.btLogin = QtGui.QPushButton(registerWidget)
        self.btLogin.setGeometry(QtCore.QRect(160, 180, 91, 31))
        self.btLogin.setObjectName(_fromUtf8("btLogin"))
        self.label = QtGui.QLabel(registerWidget)
        self.label.setGeometry(QtCore.QRect(43, 60, 71, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditPass_2 = QtGui.QLineEdit(registerWidget)
        self.lineEditPass_2.setGeometry(QtCore.QRect(130, 140, 191, 20))
        self.lineEditPass_2.setObjectName(_fromUtf8("lineEditPass_2"))
        self.labelPass_2 = QtGui.QLabel(registerWidget)
        self.labelPass_2.setGeometry(QtCore.QRect(33, 140, 81, 20))
        self.labelPass_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPass_2.setObjectName(_fromUtf8("labelPass_2"))
        self.btClose = QtGui.QPushButton(registerWidget)
        self.btClose.setGeometry(QtCore.QRect(370, 0, 31, 23))
        self.btClose.setText(_fromUtf8(""))
        self.btClose.setObjectName(_fromUtf8("btClose"))

        self.retranslateUi(registerWidget)
        QtCore.QMetaObject.connectSlotsByName(registerWidget)

    def retranslateUi(self, registerWidget):
        registerWidget.setWindowTitle(_translate("registerWidget", "注册", None))
        self.labelPass.setText(_translate("registerWidget", "密码：", None))
        self.btLogin.setText(_translate("registerWidget", "注册", None))
        self.label.setText(_translate("registerWidget", "用户名：", None))
        self.labelPass_2.setText(_translate("registerWidget", "确认密码：", None))

