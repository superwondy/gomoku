# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gameroom.ui'
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

class Ui_gameRoom(object):
    def setupUi(self, gameRoom):
        gameRoom.setObjectName(_fromUtf8("gameRoom"))
        gameRoom.resize(819, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icon/unplay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gameRoom.setWindowIcon(icon)
        gameRoom.setStyleSheet(_fromUtf8("QWidget{\n"
"}\n"
"\n"
"QFrame,QGroupBox,QPushButton,QLabel,QLineEdit,QTextEdit{\n"
"    image: url();\n"
"}\n"
"\n"
"QLabel#pannelHeader{\n"
"    background-image: url(:/image/image/pannelheader.png);\n"
"}\n"
"\n"
"QLabel#labelTable1{\n"
"    image: url(:/image/image/arrow.png);\n"
"}\n"
"\n"
"QLabel#labelTable2{\n"
"    image: url(:/image/image/arrow.png);\n"
"}\n"
"\n"
"QPushButton#bt_0{\n"
"    image: url(:/icon/icon/unplay.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_0:hover{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_0:!enabled{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_1{\n"
"    image: url(:/icon/icon/unplay.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_1:hover{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_1:!enabled{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_2{\n"
"    image: url(:/icon/icon/unplay.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_2:hover{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_2:!enabled{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_3{\n"
"    image: url(:/icon/icon/unplay.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_3:hover{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QPushButton#bt_3:!enabled{\n"
"    image: url(:/icon/icon/player.png);\n"
"    border-radius:5px;\n"
"    padding:2px 4px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(gameRoom)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pannelHeader = QtGui.QLabel(self.centralwidget)
        self.pannelHeader.setGeometry(QtCore.QRect(0, 0, 816, 101))
        self.pannelHeader.setText(_fromUtf8(""))
        self.pannelHeader.setObjectName(_fromUtf8("pannelHeader"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 211, 495))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.editMsg = QtGui.QTextEdit(self.groupBox)
        self.editMsg.setGeometry(QtCore.QRect(10, 270, 195, 181))
        self.editMsg.setObjectName(_fromUtf8("editMsg"))
        self.lineMsg = QtGui.QLineEdit(self.groupBox)
        self.lineMsg.setGeometry(QtCore.QRect(8, 470, 158, 20))
        self.lineMsg.setObjectName(_fromUtf8("lineMsg"))
        self.btSendMsg = QtGui.QPushButton(self.groupBox)
        self.btSendMsg.setGeometry(QtCore.QRect(166, 470, 41, 23))
        self.btSendMsg.setObjectName(_fromUtf8("btSendMsg"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 195, 255))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 110, 591, 481))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.bt_0 = QtGui.QPushButton(self.frame)
        self.bt_0.setGeometry(QtCore.QRect(100, 70, 100, 100))
        self.bt_0.setText(_fromUtf8(""))
        self.bt_0.setObjectName(_fromUtf8("bt_0"))
        self.bt_1 = QtGui.QPushButton(self.frame)
        self.bt_1.setGeometry(QtCore.QRect(330, 70, 100, 100))
        self.bt_1.setText(_fromUtf8(""))
        self.bt_1.setObjectName(_fromUtf8("bt_1"))
        self.bt_2 = QtGui.QPushButton(self.frame)
        self.bt_2.setGeometry(QtCore.QRect(100, 280, 100, 100))
        self.bt_2.setText(_fromUtf8(""))
        self.bt_2.setObjectName(_fromUtf8("bt_2"))
        self.bt_3 = QtGui.QPushButton(self.frame)
        self.bt_3.setGeometry(QtCore.QRect(330, 280, 100, 100))
        self.bt_3.setText(_fromUtf8(""))
        self.bt_3.setObjectName(_fromUtf8("bt_3"))
        self.labelTable1 = QtGui.QLabel(self.frame)
        self.labelTable1.setGeometry(QtCore.QRect(190, 90, 161, 81))
        self.labelTable1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTable1.setObjectName(_fromUtf8("labelTable1"))
        self.labelTable2 = QtGui.QLabel(self.frame)
        self.labelTable2.setGeometry(QtCore.QRect(190, 300, 161, 81))
        self.labelTable2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTable2.setObjectName(_fromUtf8("labelTable2"))
        self.lb_1 = QtGui.QLabel(self.frame)
        self.lb_1.setGeometry(QtCore.QRect(120, 170, 54, 12))
        self.lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_1.setObjectName(_fromUtf8("lb_1"))
        self.lb_2 = QtGui.QLabel(self.frame)
        self.lb_2.setGeometry(QtCore.QRect(360, 170, 54, 12))
        self.lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_2.setObjectName(_fromUtf8("lb_2"))
        self.lb_3 = QtGui.QLabel(self.frame)
        self.lb_3.setGeometry(QtCore.QRect(120, 380, 54, 12))
        self.lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_3.setObjectName(_fromUtf8("lb_3"))
        self.lb_4 = QtGui.QLabel(self.frame)
        self.lb_4.setGeometry(QtCore.QRect(360, 380, 54, 12))
        self.lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_4.setObjectName(_fromUtf8("lb_4"))
        self.table1 = QtGui.QLabel(self.frame)
        self.table1.setGeometry(QtCore.QRect(70, 440, 54, 12))
        self.table1.setObjectName(_fromUtf8("table1"))
        self.table2 = QtGui.QLabel(self.frame)
        self.table2.setGeometry(QtCore.QRect(170, 440, 54, 12))
        self.table2.setObjectName(_fromUtf8("table2"))
        self.table3 = QtGui.QLabel(self.frame)
        self.table3.setGeometry(QtCore.QRect(260, 440, 54, 12))
        self.table3.setObjectName(_fromUtf8("table3"))
        self.table4 = QtGui.QLabel(self.frame)
        self.table4.setGeometry(QtCore.QRect(350, 440, 54, 12))
        self.table4.setObjectName(_fromUtf8("table4"))
        gameRoom.setCentralWidget(self.centralwidget)

        self.retranslateUi(gameRoom)
        QtCore.QMetaObject.connectSlotsByName(gameRoom)

    def retranslateUi(self, gameRoom):
        gameRoom.setWindowTitle(_translate("gameRoom", "游戏大厅", None))
        self.btSendMsg.setText(_translate("gameRoom", "发送", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("gameRoom", "房间1", None))
        item = self.listWidget.item(1)
        item.setText(_translate("gameRoom", "房间2", None))
        item = self.listWidget.item(2)
        item.setText(_translate("gameRoom", "房间3", None))
        item = self.listWidget.item(3)
        item.setText(_translate("gameRoom", "房间4", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.labelTable1.setText(_translate("gameRoom", "桌子一", None))
        self.labelTable2.setText(_translate("gameRoom", "桌子二", None))
        self.lb_1.setText(_translate("gameRoom", "空座", None))
        self.lb_2.setText(_translate("gameRoom", "空座", None))
        self.lb_3.setText(_translate("gameRoom", "空座", None))
        self.lb_4.setText(_translate("gameRoom", "空座", None))
        self.table1.setText(_translate("gameRoom", "T_0_0_0", None))
        self.table2.setText(_translate("gameRoom", "T_0_1_0", None))
        self.table3.setText(_translate("gameRoom", "T_1_0_0", None))
        self.table4.setText(_translate("gameRoom", "T_1_1_0", None))

import gameroom_rc
