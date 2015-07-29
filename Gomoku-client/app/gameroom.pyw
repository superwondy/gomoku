#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# gameroom.py - network data stream operation interface
#
# NOTE: 游戏大厅窗口类
#                                                                                                                                                                        
#======================================================================
import json
import time
import threading
import logging
import random

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QButtonGroup
from ui.ui_gameroom import Ui_gameRoom
from client import GomokuClient
from gomokuwindow import GomokuWindow
import lib.datatag as dtag
import lib.log as log
from lib.service import service

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

TABLE_OFFSET_X = 110
TABLE_OFFSET_Y = 70
TABLE_PADDING_X = 50
TABLE_PADDING_Y = 50

logger = log.get_logger('GameRoom')
#======================================================================
# GameRoom--大厅窗口类
#======================================================================
class GameRoom(QtGui.QMainWindow, Ui_gameRoom, service):
    """docstring for GameRoom"""
    global logger
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        service.__init__(self)
        # service.__init__(self, self.__class__.SERVICE_ID)
        self.setupUi(self)

        self._init_attr()
        self.__init_ui()
        self.set_action()

    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
    	commands = {
            dtag.PLAYERS_CHAT:      self.handle_players_chat,
            dtag.UPDATE_STATE:      self.handle_update_room_state,
            dtag.GET_ROOM:          self.handle_get_room
        }

        self.username = 'user'
    	# self.shutdown = False
        self.client = None
        self.tables = None
        self.t1 = None
        self.hid = None
        self.btgroup = QButtonGroup()
        self.timer = QTimer()
        self.gomoku = None
        self.cur_room_id = 0

        self.registers(commands)

    def __init_ui(self):
        self.pannelHeader.setPixmap(QPixmap(_fromUtf8(":/image/image/pannelheader.png")))
        self.btgroup.addButton(self.bt_0, 1)
        self.btgroup.addButton(self.bt_1, 2)
        self.btgroup.addButton(self.bt_2, 3)
        self.btgroup.addButton(self.bt_3, 4)

        # 对应座位下标
        self.lbgroup = []
        self.lbgroup.append(self.lb_1)
        self.lbgroup.append(self.lb_2)
        self.lbgroup.append(self.lb_3)
        self.lbgroup.append(self.lb_4)

        # 记录桌子的房间编号
        self.tbgroup = []
        self.tbgroup.append(self.table1)
        self.tbgroup.append(self.table2)
        self.tbgroup.append(self.table3)
        self.tbgroup.append(self.table4)
        self.table1.hide()
        self.table2.hide()
        self.table3.hide()
        self.table4.hide()

    def set_gomoku(self, gomoku):
    	self.gomoku = gomoku

    def set_client(self, client):
        self.client = client
        self.hid = client.hid

    def set_user_name(self, username):
        self.username = username

    def get_table_name(self, index):
        table_index = self.lbgroup[index]
        table_name = self.tbgroup[index]
        return table_index, table_name

    #----------------------------------------------------------------------
    # 大厅事件处理
    #----------------------------------------------------------------------

    # 显示房间桌子状态
    def _show_room(self, item):
        if item:
            self.cur_room_id = self.listWidget.row(item)
        self.update_room_state(self.cur_room_id)

    # 进入游戏
    def enter_game(self, button):
        logger.debug('enter_game_fun' + str(button.objectName()))

        bttext = str(button.objectName())
        bt_name = bttext.split('_')
        index = bt_name[1]

        index = int(index)

        table_name = str(self.tbgroup[index].text())
        ls = table_name.split('_')
        room = int(ls[3])
        table = int(ls[1])
        seat = int(ls[2])
        self.gomoku.set_room_table_seat(room, table, seat)
        self.gomoku.show()
        self.showMinimized()

        table_index = self.lbgroup[index]
        table_index.setText(_fromUtf8('有人'))
        button.setDisabled(True)

        #注册服务端房间信息
        jdata = {}
        jdata['tag'] = dtag.ENTER_ROOM
        jdata['room'] = room
        jdata['table'] = table
        jdata['seat'] = seat
        self.client.send(json.dumps(jdata))

    # 申请更新房间状态
    def get_tables(self):
        jdata = {}
        jdata['tag'] = dtag.GET_ROOM
        self.client.send(json.dumps(jdata))
        pass

    # 发送大厅聊天信息
    def bt_send_msg(self):
        text = unicode(self.lineMsg.text())
        jdata = {}
        jdata['tag'] = dtag.PLAYERS_CHAT
        jdata['user'] = self.username
        jdata['msg'] = text.encode('utf-8')
        self.client.send(json.dumps(jdata))
        msg = unicode(self.editMsg.toPlainText())
        if len(msg) > 1024:
            msg = msg[1024/2:]
        msg = msg + u'我:' + text + '\n'
        self.editMsg.setText(_fromUtf8(msg))
        self.lineMsg.setText('')

    # 注册大厅响应事件
    def set_action(self):
        self.listWidget.itemDoubleClicked.connect(self._show_room)
        self.btgroup.buttonClicked.connect(self.enter_game)
        self.btSendMsg.clicked.connect(self.bt_send_msg)
        self.lineMsg.returnPressed.connect(self.bt_send_msg)

    #----------------------------------------------------------------------
    # 大厅消息处理句柄
    #----------------------------------------------------------------------

    def handle_players_chat(self, jdata):
        msg = unicode(self.editMsg.toPlainText())
        if len(msg) > 1024:
            msg = msg[1024/2:]
        msg = msg + jdata['user'] + ':' + jdata['msg'] + '\n'
        self.editMsg.setText(_fromUtf8(msg))

    def handle_update_room_state(self, jdata):
        logger.debug('handle_update_room_state')
        self.tables = jdata['rooms']
        self.update_room_state(self.cur_room_id)

    def handle_get_room(self, jdata):
        logger.debug('handle_get_room')
        self.tables = jdata['rooms']
        self.update_room_state(self.cur_room_id)

    def handle_enter_room(self, jdata):
        self.labelUserName.setText(_fromUtf8(self.username))

    #----------------------------------------------------------------------
    # 更新大厅状态
    #----------------------------------------------------------------------

    # 更新房间桌子状态
    def update_room_state(self, room_id):
        row = 1
        column = 1
        count = 0
        room_table = self.tables[room_id]
        buttons = self.btgroup.buttons()
        for tb in room_table:
            for seat in tb:
                table_index, table_name = self.get_table_name(count)

                button = buttons[count]
                name = table_name.text()
                name = name[:-2] + '_' + str(room_id)
                table_name.setText(_fromUtf8(name))
                if seat == 0:
                    table_index.setText(_fromUtf8('空座'))
                    button.setEnabled(True)
                else:
                    table_index.setText(_fromUtf8('有人'))
                    button.setDisabled(True)
                column += 1
                count += 1
            row += 1
        self.update()

if __name__ == '__main__':
        import sys
        app = QtGui.QApplication(sys.argv)
        app.setApplicationName("GameRoom Pannel")
        app.setQuitOnLastWindowClosed(True)

        window = GameRoom()
        window.show()
        sys.exit(app.exec_())
