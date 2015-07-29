#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# server.py - 
#                                                                                                                                                         
#======================================================================
import time
import json

import sys
sys.path.append("..")
import lib.netstream as ns
import lib.datatag as dtag
import lib.log as log
from lib.dispatcher import dispatcher

from game import GomokuGame
from sqlitedb import SqliteDb
from roomservice import RoomService
from gameservice import GameService

#======================================================================
# 头定义数据
#======================================================================


logger = log.get_logger('MainServer')
#======================================================================
# 服务端主类
#======================================================================
class MainServer(object):
    """docstring for MainServer"""
    def __init__(self, **kwargs):
        super(MainServer, self).__init__()

        self.port = 8888
        self.header = 8
        self.shutdown = False

        if 'port' in kwargs:
            self.port = kwargs['port']
        if 'header' in kwargs:
            self.header = kwargs['header']

        self._init_attr()

    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
        self.host = ns.nethost(self.header)
        self.clients = {}
        self.db = SqliteDb()

        # 大厅服务代理
        self.roomservice = RoomService()
        self.roomservice.set_host(self.host)
        self.roomservice.set_clients(self.clients)
        self.roomservice.set_db(self.db)
        # 游戏流程服务代理

        self.gameservice = GameService()
        self.gameservice.set_host(self.host)
        self.gameservice.set_clients(self.clients)
        self.gameservice.set_db(self.db)
        #创建消息处理分发器
        self.dispatch = dispatcher()

        #向分发器注册两个窗口类
        self.dispatch.register(self.roomservice.SID, self.roomservice)
        self.dispatch.register(self.gameservice.SID, self.gameservice)

    def startup(self):
        self.host.startup(self.port)

    def send(self, hid, data):
        self.host.send(hid, data)

    #----------------------------------------------------------------------
    # 游戏流程处理
    #----------------------------------------------------------------------

    # 玩家申请游戏开始
    def require_game_start(self, hid, jdata):
        self.send(hid, json.dumps(jdata))

    #消息分发处理
    def patcher_data(self, hid, data):
        jdata = json.loads(data)
        tag = jdata['tag']

        jdata['hid'] = hid
        # 专属游戏界面端消息
        if tag in (dtag.MOVE, dtag.BACK_MOVE, dtag.BACK_MOVE_REPLY, dtag.PLAYER_CHAT, dtag.GAME_GIVE_UP, dtag.REQUIRE_USER_INFO):
            jdata['sid'] = self.gameservice.SID
            self.dispatch.dispatch(jdata, self.gameservice)

        # 专属大厅消息
        elif tag in (dtag.ROOM_LOGIN, dtag.GET_ROOM, dtag.PLAYERS_CHAT):
            jdata['sid'] = self.roomservice.SID
            self.dispatch.dispatch(jdata, self.roomservice)

        # 同时通知游戏界面和大厅更新消息
        elif tag in (dtag.ENTER_ROOM, dtag.GAME_LEAVE):
            jdata['sid'] = self.roomservice.SID
            self.dispatch.dispatch(jdata, self.roomservice)

            jdata['sid'] = self.gameservice.SID
            self.dispatch.dispatch(jdata, self.gameservice)

        elif tag == dtag.CLOSE_CLIENT:
            jdata['sid'] = self.roomservice.SID
            self.dispatch.dispatch(jdata, self.roomservice)

            jdata['sid'] = self.gameservice.SID
            self.dispatch.dispatch(jdata, self.gameservice)
            del self.clients[hid]

    # 新客户端接入
    def new_client(self, hid):
        self.clients[hid] = {}
        jdata = {}
        jdata['tag'] = dtag.NEW_CLIENT
        jdata['hid'] = hid
        self.host.send(hid, json.dumps(jdata))

    # 客户端失去连接
    def lose_connect(self, hid):
        # 如果失去连接，则默认对手赢
        opponent = self.clients.get(hid).get('opponent')
        if opponent:
            self.gameservice.win_notion(hid, False, True)
            self.gameservice.win_notion(opponent, True, True)

    #----------------------------------------------------------------------
    # 主消息分发函数
    #----------------------------------------------------------------------
    def process(self):
        while not self.shutdown:
            if self.host.state == 0:
                self.host.startup()
            time.sleep(0.1)
            self.host.process()
            event, wparam, lparam, data = self.host.read()
            if event < 0: continue
            if event == ns.NET_DATA:    #new data
                self.patcher_data(wparam, data)
            elif event == ns.NET_NEW:   #new client
                logger.debug('new client')
                self.new_client(wparam)
            elif event == ns.NET_LEAVE:
                logger.debug('connect lose')
                self.lose_connect(wparam)

#----------------------------------------------------------------------
# testing case
#----------------------------------------------------------------------
if __name__ == '__main__':
    server = GomokuServer()
    server.startup()
    server.process()
