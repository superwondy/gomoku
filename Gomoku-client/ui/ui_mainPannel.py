# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainPannel.ui'
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

class Ui_mainPannel(object):
    def setupUi(self, mainPannel):
        mainPannel.setObjectName(_fromUtf8("mainPannel"))
        mainPannel.resize(900, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icon/appicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainPannel.setWindowIcon(icon)
        mainPannel.setStyleSheet(_fromUtf8("QWidget{\n"
"}\n"
"\n"
"QGroupBox,QGraphicsView,QPushButton,QLabel,QLineEdit,QTextEdit{\n"
"    background-image: url();\n"
"}\n"
"\n"
"QGroupBox{\n"
"}\n"
"\n"
"QLabel#pannelHeader{\n"
"    background-image: url(:/image/image/pannelheader.png);\n"
"}\n"
"\n"
"QPushButton#btMenu{\n"
"    image: url(:/icon/icon/appicon.png);\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QLabel#labelState{\n"
"    font: 75 12pt \"Adobe 宋体 Std L\";\n"
"}\n"
"\n"
"QPushButton#btClose{\n"
"    image: url(:/icon/icon/close.png);\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QLabel,QPushButton,QCheckBox,QComboBox{\n"
"    border-width:0;\n"
"    border-image: url(:);\n"
"}"))
        self.centralwidget = QtGui.QWidget(mainPannel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBoxL = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxL.setGeometry(QtCore.QRect(0, 100, 191, 505))
        self.groupBoxL.setTitle(_fromUtf8(""))
        self.groupBoxL.setObjectName(_fromUtf8("groupBoxL"))
        self.lPlayer = QtGui.QLabel(self.groupBoxL)
        self.lPlayer.setGeometry(QtCore.QRect(23, 10, 161, 181))
        self.lPlayer.setText(_fromUtf8(""))
        self.lPlayer.setObjectName(_fromUtf8("lPlayer"))
        self.leftEditvectory = QtGui.QLineEdit(self.groupBoxL)
        self.leftEditvectory.setGeometry(QtCore.QRect(70, 200, 113, 20))
        self.leftEditvectory.setReadOnly(True)
        self.leftEditvectory.setObjectName(_fromUtf8("leftEditvectory"))
        self.btVectoryL = QtGui.QPushButton(self.groupBoxL)
        self.btVectoryL.setGeometry(QtCore.QRect(10, 200, 51, 23))
        self.btVectoryL.setFlat(True)
        self.btVectoryL.setObjectName(_fromUtf8("btVectoryL"))
        self.labelleftuser = QtGui.QLabel(self.groupBoxL)
        self.labelleftuser.setGeometry(QtCore.QRect(140, 10, 51, 31))
        self.labelleftuser.setText(_fromUtf8(""))
        self.labelleftuser.setObjectName(_fromUtf8("labelleftuser"))
        self.btBackmove = QtGui.QPushButton(self.groupBoxL)
        self.btBackmove.setGeometry(QtCore.QRect(30, 280, 131, 31))
        self.btBackmove.setObjectName(_fromUtf8("btBackmove"))
        self.btDrawGame = QtGui.QPushButton(self.groupBoxL)
        self.btDrawGame.setGeometry(QtCore.QRect(30, 360, 131, 31))
        self.btDrawGame.setObjectName(_fromUtf8("btDrawGame"))
        self.btGiveUp = QtGui.QPushButton(self.groupBoxL)
        self.btGiveUp.setGeometry(QtCore.QRect(30, 320, 131, 31))
        self.btGiveUp.setObjectName(_fromUtf8("btGiveUp"))
        self.btGameStart = QtGui.QPushButton(self.groupBoxL)
        self.btGameStart.setGeometry(QtCore.QRect(30, 240, 131, 31))
        self.btGameStart.setObjectName(_fromUtf8("btGameStart"))
        self.labelInTurn = QtGui.QLabel(self.groupBoxL)
        self.labelInTurn.setGeometry(QtCore.QRect(135, 170, 52, 31))
        self.labelInTurn.setFrameShadow(QtGui.QFrame.Plain)
        self.labelInTurn.setText(_fromUtf8(""))
        self.labelInTurn.setObjectName(_fromUtf8("labelInTurn"))
        self.labelState = QtGui.QLabel(self.groupBoxL)
        self.labelState.setGeometry(QtCore.QRect(10, 420, 171, 51))
        self.labelState.setAlignment(QtCore.Qt.AlignCenter)
        self.labelState.setObjectName(_fromUtf8("labelState"))
        self.pannelHeader = QtGui.QLabel(self.centralwidget)
        self.pannelHeader.setGeometry(QtCore.QRect(0, 0, 901, 101))
        self.pannelHeader.setText(_fromUtf8(""))
        self.pannelHeader.setObjectName(_fromUtf8("pannelHeader"))
        self.groupBoxR = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxR.setGeometry(QtCore.QRect(700, 100, 191, 505))
        self.groupBoxR.setTitle(_fromUtf8(""))
        self.groupBoxR.setObjectName(_fromUtf8("groupBoxR"))
        self.rPlayer = QtGui.QLabel(self.groupBoxR)
        self.rPlayer.setGeometry(QtCore.QRect(23, 10, 161, 181))
        self.rPlayer.setText(_fromUtf8(""))
        self.rPlayer.setObjectName(_fromUtf8("rPlayer"))
        self.rightEditvectory = QtGui.QLineEdit(self.groupBoxR)
        self.rightEditvectory.setGeometry(QtCore.QRect(70, 200, 113, 20))
        self.rightEditvectory.setEchoMode(QtGui.QLineEdit.NoEcho)
        self.rightEditvectory.setDragEnabled(False)
        self.rightEditvectory.setReadOnly(True)
        self.rightEditvectory.setObjectName(_fromUtf8("rightEditvectory"))
        self.btVectoryR = QtGui.QPushButton(self.groupBoxR)
        self.btVectoryR.setGeometry(QtCore.QRect(10, 200, 51, 23))
        self.btVectoryR.setFlat(True)
        self.btVectoryR.setObjectName(_fromUtf8("btVectoryR"))
        self.labelrightuser = QtGui.QLabel(self.groupBoxR)
        self.labelrightuser.setGeometry(QtCore.QRect(20, 10, 61, 31))
        self.labelrightuser.setText(_fromUtf8(""))
        self.labelrightuser.setObjectName(_fromUtf8("labelrightuser"))
        self.editMsg = QtGui.QTextEdit(self.groupBoxR)
        self.editMsg.setGeometry(QtCore.QRect(10, 250, 171, 191))
        self.editMsg.setObjectName(_fromUtf8("editMsg"))
        self.lineMsg = QtGui.QLineEdit(self.groupBoxR)
        self.lineMsg.setGeometry(QtCore.QRect(10, 460, 141, 20))
        self.lineMsg.setObjectName(_fromUtf8("lineMsg"))
        self.btSendMsg = QtGui.QPushButton(self.groupBoxR)
        self.btSendMsg.setGeometry(QtCore.QRect(154, 460, 38, 23))
        self.btSendMsg.setObjectName(_fromUtf8("btSendMsg"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 110, 495, 495))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.btClose = QtGui.QPushButton(self.centralwidget)
        self.btClose.setGeometry(QtCore.QRect(860, 0, 40, 40))
        self.btClose.setText(_fromUtf8(""))
        self.btClose.setObjectName(_fromUtf8("btClose"))
        self.btMenu = QtGui.QPushButton(self.centralwidget)
        self.btMenu.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btMenu.setText(_fromUtf8(""))
        self.btMenu.setObjectName(_fromUtf8("btMenu"))
        mainPannel.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainPannel)
        QtCore.QMetaObject.connectSlotsByName(mainPannel)

    def retranslateUi(self, mainPannel):
        mainPannel.setWindowTitle(_translate("mainPannel", "Gomoku", None))
        self.btVectoryL.setText(_translate("mainPannel", "战绩", None))
        self.btBackmove.setText(_translate("mainPannel", "悔棋", None))
        self.btDrawGame.setText(_translate("mainPannel", "和棋", None))
        self.btGiveUp.setText(_translate("mainPannel", "认输", None))
        self.btGameStart.setText(_translate("mainPannel", "准备游戏", None))
        self.labelState.setText(_translate("mainPannel", "等待玩家进入", None))
        self.btVectoryR.setText(_translate("mainPannel", "战绩", None))
        self.btSendMsg.setText(_translate("mainPannel", "发送", None))

import mainPannel_rc
