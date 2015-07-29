#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# graphicview.py
#
# NOTE: 游戏大厅窗口类
#                                                                                                                                                                        
#======================================================================
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QGraphicsView
from PyQt4.QtGui import QPixmap, QGraphicsScene, QGraphicsPixmapItem

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MygraphicView(QGraphicsView):
	"""docstring for MygraphicView"""
	def __init__(self, parent=None):
		super(QGraphicsView, self).__init__(parent)
		self.flag = None
	
	def set_item(self, flag):
		self.flag = flag

	def new_item(self, x, y):
		pass

	def mouseMoveEvent(self, event):
		print event.pos()
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            self.new_item(x, y)