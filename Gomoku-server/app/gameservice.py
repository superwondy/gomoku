#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

# import sys
# sys.path.append("..")

import lib.datatag as dtag
import lib.log as log
from lib.service import service
from game import GomokuGame

#======================================================================
# format of headers
#======================================================================
#游戏状态信息
GAME_REDEAY = 1
GAME_START = 2
GAME_HOLD_UP = 3
GAME_PLAYING = 4
GAME_WAITING = 5
GAME_STOP = 6
GAME_IN_TURN = 7
GAME_NOT_IN_TURN = 8

logger = log.get_logger('GameService')

class GameService(service):
    """docstring for game_service"""
    
    def __init__(self):
        service.__init__(self)

        self._init_attr()


    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
        commands = {
            dtag.MOVE:              self.handle_play_one_move,
            dtag.BACK_MOVE:         self.handle_back_move,
            dtag.BACK_MOVE_REPLY:   self.handle_back_move_reply,
            dtag.PLAYER_CHAT:       self.handle_player_chat,
            dtag.ENTER_ROOM:        self.hanlde_enter_room,
            dtag.CLOSE_CLIENT:      self.handle_client_close,
            dtag.GAME_GIVE_UP:      self.handle_game_give_up,
            dtag.GAME_LEAVE:        self.handle_game_leave,
            dtag.REQUIRE_USER_INFO: self.handle_query_user_info
        }
        self.registers(commands)

        self.host = None
        self.clients = None
        self.db = None
        self.games = {}

    def set_host(self, host):
        self.host = host

    def set_clients(self, clients):
        self.clients = clients

    def set_db(self, db):
        self.db = db

    #----------------------------------------------------------------------
    # 信息处理句柄
    #----------------------------------------------------------------------

    # 玩家下一步棋
    def handle_play_one_move(self, jdata):
        hid = jdata['hid']
        room = self.clients[hid]['room']
        table = self.clients[hid]['table']
        game = self.get_game(hid, room, table)
        win = game.play_one_step(hid, jdata['row'], jdata['column'])

        jdata['tag'] = dtag.MOVE
        opponent = self.clients.get(hid).get('opponent')
        if opponent:
            self.host.send(opponent, json.dumps(jdata))
        
        if win and opponent:
            self.win_notion(hid, True)
            self.win_notion(opponent, False)

    def handle_player_chat(self, jdata):
        hid = jdata['hid']
        del jdata['hid']
        opponent = self.get_opponent(hid)
        if opponent:
            self.host.send(opponent, json.dumps(jdata))

    def handle_back_move(self, jdata):
        hid = jdata['hid']
        del jdata['hid']
        opponent = self.get_opponent(hid)
        if opponent:
            self.host.send(opponent, json.dumps(jdata))

    def handle_back_move_reply(self, jdata):
        hid = jdata['hid']
        del jdata['hid']
        opponent = self.get_opponent(hid)
        if opponent:
            self.host.send(opponent, json.dumps(jdata))
            reply = jdata['reply']
            if reply:
                room = self.clients[hid]['room']
                table = self.clients[hid]['table']
                game = self.get_game(hid, room, table)
                game.back_move()

    # 有玩家进入房间
    def hanlde_enter_room(self, jdata):
        hid = jdata['hid']
        room = jdata['room']
        table = jdata['table']
        seat = jdata['seat']
        
        self.clients[hid]['room'] = room
        self.clients[hid]['table'] = table
        self.clients[hid]['seat'] = seat

        opponent = self.get_opponent(hid)

        if opponent:
            #更改玩家状态信息
            data = {}
            data['tag'] = dtag.GAME_STATE
            data['state'] = GAME_START
            #通知对手开始
            op_name = self.clients[opponent]['name']
            result = self.db.select_by_name(op_name)
            if result:
                uid, name, score = result
                data['op_name'] = op_name
                data['op_score'] = score
            self.host.send(opponent, json.dumps(data))

            #自己进入准备状态
            data['state'] = GAME_REDEAY
            self.host.send(hid, json.dumps(data))
        else:
            #没有其他玩家在桌子上
            data = {}
            data['tag'] = dtag.GAME_STATE
            data['state'] = GAME_REDEAY
            self.host.send(hid, json.dumps(data))

    def handle_game_leave(self, jdata):
        hid = jdata['hid']
        room = self.clients[hid]['room']
        table = self.clients[hid]['table']
        opponent = self.clients[hid]['opponent']
        if opponent:
            self.win_notion(opponent, True, True)
        key = str(room) + '-' + str(table)
        if key in self.games.keys():
            del self.games[key]

    def handle_game_give_up(self, jdata):
        hid = jdata['hid']
        opponent = self.get_opponent(hid)
        if opponent:
            jdata['tag'] = dtag.GAME_WIN
            jdata['result'] = 'giveup'
            self.host.send(opponent, json.dumps(jdata))

    def handle_client_close(self, jdata):
        self.handle_game_leave(jdata)

    def handle_query_user_info(self, jdata):
        hid = jdata['hid']
        name = jdata['name']
        result = self.db.select_by_name(name)
        if not result:
            self.db.insert_db(name)
            result = self.db.select_by_name(name)

        uid, user, score = result
        data = {}
        data['tag'] = dtag.USER_INFO_REPLY
        data['uid'] = uid
        data['name'] = name
        data['score'] = score
        self.host.send(hid, json.dumps(data))

    #----------------------------------------------------------------------
    # 辅助操作函数
    #----------------------------------------------------------------------

    def get_game(self, hid, room, table):
        key = str(room) + '-' + str(table)
        game = self.games.get(key)
        if not game:
            game = GomokuGame()
            game.set_bplayer(hid)
            opponent = self.get_opponent(hid)
            game.set_wplayer(opponent)
            self.games[key] = game
        return game

    def get_opponent(self, hid):
        data = self.clients.get(hid)
        opponent = data.get('opponent')
        return opponent

    # 玩家输赢提示
    def win_notion(self, hid, win, lose=False):
        logger.debug('玩家' + str(hid) + '赢-' + str(win))
        jdata = {}
        jdata['tag'] = dtag.GAME_WIN
        if win:
            jdata['result'] = 'win'
        else:
            jdata['result'] = 'lose'

        if lose:
            jdata['lose'] = True
        else:
            jdata['lose'] = False
        self.host.send(hid, json.dumps(jdata))

    def leave_game(self, hid):
        room = self.clients[hid]['room']
        table = self.clients[hid]['table']

        key = str(room) + '-' + str(table)
        del self.game[key]
        del self.clients[hid]

    def send(self, hid, data):
        self.host.send(hid, data)