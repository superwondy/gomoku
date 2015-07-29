#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import threading
import logging
import random

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QButtonGroup
from ui.ui_login import Ui_loginWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Login(QtGui.QWidget, Ui_loginWidget):
    """docstring for Login"""
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
        self.setupUi(self)

        self.__init_attr()

        # self.btLogin.setFocus()
        self.set_action()
        
    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def __init_attr(self):
        self.isOnDrag = False

    def notice(self, text):
        self.labelNotice.setText(_fromUtf8(text))

    def set_action(self):
        self.btClose.clicked.connect(self.close)

    #----------------------------------------------------------------------
    # 鼠标事件处理
    #----------------------------------------------------------------------
    def mouseMoveEvent(self, event):
        if self.isOnDrag:
            self.move(event.globalPos()-self.dragPosition)

    def mousePressEvent(self, event):
        print event.pos()
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.pos()
            if self.dragPosition.y() <= 40:
                self.isOnDrag = True

    def mouseReleaseEvent(self, event):
        self.isOnDrag = False
