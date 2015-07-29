#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import lib.log as log
import lib.datatag as dtag

# import sys
# sys.path.append("..")
from lib.service import service

#======================================================================
# 头定义数据
#======================================================================
ROOM_NUM = 4
TABLE_NUM = 2
TABLE_PLAYER_NUM = 2


logger = log.get_logger('RoomService')
class RoomService(service):
    """docstring for room_service"""

    def __init__(self):
        service.__init__(self)

        self._init_attr()


    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
        commands = {
            dtag.ENTER_ROOM:        self.handle_enter_room,
            dtag.PLAYERS_CHAT:      self.handle_players_chat,
            dtag.GET_ROOM:          self.handle_get_room,
            dtag.CLOSE_CLIENT:      self.handle_client_close,
            dtag.GAME_LEAVE:        self.handle_game_leave,
            dtag.ROOM_LOGIN:        self.handle_login
        }
        self.registers(commands)

        self.tables = [[[0 for player in range(TABLE_PLAYER_NUM)] for col in range(TABLE_NUM)] for row in range(ROOM_NUM)]
        self.host = None
        self.clients = None
        self.db = None

    def set_host(self, host):
        self.host = host

    def set_clients(self, clients):
        self.clients = clients

    def set_db(self, db):
        self.db = db
    #----------------------------------------------------------------------
    # 信息处理句柄
    #----------------------------------------------------------------------

    # 有玩家进入房间
    def handle_enter_room(self, jdata):
        hid = jdata['hid']
        room = jdata['room']
        table = jdata['table']
        seat = jdata['seat']
        
        self.clients[hid]['room'] = room
        self.clients[hid]['table'] = table
        self.clients[hid]['seat'] = seat

        tab = self.tables[room][table]
        index = (seat+1) % TABLE_PLAYER_NUM
        opponent = tab[index]

        if opponent != 0:
            self.clients[hid]['opponent'] = opponent
            self.clients[opponent]['opponent'] = hid

        self.tables[room][table][seat] = hid

        #更新登录用户的大厅信息
        data = {}
        data['tag'] = dtag.UPDATE_STATE
        data['rooms'] = self.tables
        self.update_state(hid, self.upate_room_state, data, True)

    # 更新大厅桌子信息
    def handle_get_room(self, jdata):
        hid = jdata['hid']
        jdata = {}
        jdata['tag'] = dtag.GET_ROOM
        jdata['rooms'] = self.tables
        data = json.dumps(jdata)
        self.host.send(hid, data)

    def handle_players_chat(self, jdata):
        hid = jdata['hid']
        self.update_state(hid, self.send_chat_msg, jdata)

    def handle_client_close(self, jdata):
        self.handle_game_leave(jdata)

    def handle_game_leave(self, jdata):
        hid = jdata['hid']
        self.close_client(hid)

    def handle_login(self, jdata):
        hid = jdata['hid']
        name = unicode(jdata['name'])
        result = self.db.select_by_name(name)
        print result
        data = {}
        data['tag'] = dtag.ROOM_LOGIN_REPLY
        if result:
            data['reply'] = True
        else:
            print 'no user'
            data['reply'] = False
        self.send(hid, json.dumps(data))

    def update_status(self, hid):
        jdata = {}
        jdata['tag'] = dtag.UPDATE_STATE
        jdata['msg'] = self.chattext
        jdata['rooms'] = self.tables
        self.send(hid, json.dumps(jdata))

    #----------------------------------------------------------------------
    # 辅助操作函数
    #----------------------------------------------------------------------

    # 更新客户端状态
    def update_state(self, hid, func, jdata, tosender=False):
        for key in self.clients.keys():
            if key == hid and not tosender:
                continue
            func(key, jdata)

    def upate_room_state(self, hid, jdata):
        self.send(hid, json.dumps(jdata))

    # 发送大厅聊天信息
    def send_chat_msg(self, hid, jdata):
        self.send(hid, json.dumps(jdata))

    def close_client(self, hid):
        room = self.clients[hid]['room']
        table = self.clients[hid]['table']
        seat = self.clients[hid]['seat']
        self.tables[room][table][seat] = 0

        #更新登录用户的大厅信息
        data = {}
        data['tag'] = dtag.UPDATE_STATE
        data['rooms'] = self.tables
        self.update_state(hid, self.upate_room_state, data, True)

    def send(self, hid, data):
        self.host.send(hid, data)
