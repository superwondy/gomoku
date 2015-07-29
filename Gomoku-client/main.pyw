#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import threading

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QTimer

import lib.log as log
import lib.datatag as dtag
from lib.dispatcher import dispatcher
from app.client import GomokuClient
from app.gomokuwindow import GomokuWindow
from app.gameroom import GameRoom
from app.login import Login

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

logger = log.get_logger('MainClient')
#======================================================================
# MainClient--程序主类
#======================================================================
class MainClient(object):
    """程序主类"""
    # global logger
    def __init__(self, ip='127.0.0.1', port=8888):
        super(MainClient, self).__init__()
        self.ip = ip
        self.port = port
        self.username = 'user'

        self._init_attr()
        self._set_action()
        
    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
        self.login = False
        self.loginwidget = Login()
        
        #创建大厅
        self.game_room = GameRoom()
        self.game_room.hide()
        #创建游戏面板
        self.gomoku = GomokuWindow()
        self.gomoku.hide()

        self.game_room.set_gomoku(self.gomoku)
        #创建消息接收代理服务
        self.client = GomokuClient()
        #创建消息处理分发器
        self.dispatch = dispatcher()

        #时钟
        self.timer = QTimer()

    def _set_action(self):
        self.loginwidget.btLogin.clicked.connect(self._init_login)
        self.loginwidget.lineEditIp.returnPressed.connect(self._init_login)
        self.loginwidget.lineEditPort.returnPressed.connect(self._init_login)
        self.loginwidget.lineEditName.returnPressed.connect(self._init_login)

    def user_login(self):
        self.loginwidget.show()

    def _init_login(self):
        import re
        is_ok = True
        ipAddressRegex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        regex = re.compile(ipAddressRegex)
        ip = self.loginwidget.lineEditIp.text()
        ip = str(ip)
        match = regex.match(ip)
        if match:
            self.ip = ip
        else:
            is_ok = False
            self.loginwidget.notice('Ip地址格式错误')

        port = str(self.loginwidget.lineEditPort.text())
        if port.isdigit():
            self.port = int(port)
        else:
            is_ok = False
            self.loginwidget.notice('端口必须为数字')

        username = self.loginwidget.lineEditName.text()
        username = str(username)
        if not username or username == '':
            self.loginwidget.notice('用户名不能为空')
            is_ok = False
        else:
            self.username = username

        self.client.set_ip(self.ip)
        self.client.set_port(self.port)
        self.client.startup()
        self.game_room.set_client(self.client)
        self.gomoku.set_client(self.client)

        if is_ok:
            jdata = {}
            jdata['tag'] = dtag.ROOM_LOGIN
            jdata['name'] = self.username
            self.client.send(json.dumps(jdata))
            # print '发送登录'

        self.run()

    def handl_login_reply(self, jdata):
        reply = jdata['reply']
        print reply
        if reply:
            self.enter_room()
        else:
            reply = QtGui.QMessageBox.warning(None, 'Message', \
                _fromUtf8('没有找到用户名，请试下：user1, user2'))

    def enter_room(self):
        #关闭登录窗口
        self.loginwidget.close()

        # self.client.set_ip(self.ip)
        # self.client.set_port(self.port)
        # self.client.startup()

        #显示游戏大厅
        self.game_room.show()
        # self.game_room.set_client(self.client)
        self.game_room.get_tables()
        self.game_room.set_user_name(self.username)

        #游戏主窗口属性设置
        # self.gomoku.set_client(self.client)
        self.gomoku.set_user_name(self.username)
        self.gomoku.set_parent(self.game_room)
        self.gomoku.set_user_name(self.username)

        #向分发器注册两个窗口类
        self.dispatch.register(self.game_room.SID, self.game_room)
        self.dispatch.register(self.gomoku.SID, self.gomoku)

    def run(self):
        self.timer.timeout.connect(self.process)
        self.timer.start(400)

    #消息分发处理
    def patcher_data(self, data):
        jdata = json.loads(data)
        tag = jdata['tag']

        # 专属游戏界面端消息
        if tag in (dtag.MOVE, dtag.BACK_MOVE, dtag.BACK_MOVE_REPLY, dtag.PLAYER_CHAT, dtag.GAME_WIN, dtag.GAME_STATE, dtag.USER_INFO_REPLY):
            jdata['sid'] = self.gomoku.SID
            self.dispatch.dispatch(jdata, self.gomoku)

        # 专属大厅消息
        elif tag in (dtag.PLAYERS_CHAT, dtag.GET_ROOM, dtag.UPDATE_STATE, dtag.ENTER_ROOM):
            jdata['sid'] = self.game_room.SID
            self.dispatch.dispatch(jdata, self.game_room)

        elif tag ==  dtag.ROOM_LOGIN_REPLY:
            self.handl_login_reply(jdata)
        elif tag == dtag.NEW_CLIENT:
            logger.debug('new client-----' + data)

    def process(self):
        try:
            time.sleep(0.08)
            data = self.client.recv()
            if len(data) == 0:
                return
            self.patcher_data(data)
        except Exception, e:
            raise
        else:
            pass
        finally:
            pass


#----------------------------------------------------------------------
# testing case
#----------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Main Pannel")
    app.setQuitOnLastWindowClosed(True)


    main = MainClient()

    main.user_login()

    sys.exit(app.exec_())
