#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# client.py 客户端的消息接收类
#----------------------------------------------------------------------
import time
import json
import logging
import threading

# import sys
# sys.path.append("..")
import lib.netstream as ns
import lib.datatag as dtag

logger = logging.getLogger('GomokuClient')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#======================================================================
# 头定义数据
#======================================================================
PLAYER_PLAYING = 1
PLAYER_WAITING = 2

class GomokuClient(object):
	"""客户端的消息接收类"""
	def __init__(self):
		super(GomokuClient, self).__init__()

		self._init_attr()
		pass

	def _init_attr(self):
		self.ip = '127.0.0.1'
		self.port = 8888
		self.header = 8
		self.shutdown = False
		self.sock = None
		self.hid = None
		self.uid = None
		self.status = PLAYER_WAITING
		self.tables = None
		self.room = None
		self.table = None
		self.seat = None
		self.roomchat = ''
		self.dispatch = None
		self.requires = []

	def startup(self):
		self.sock = ns.netstream(8)
		self.sock.connect(self.ip, self.port)
		self.sock.nodelay(0)
		self.sock.nodelay(1)

	def sock_on(self):
		if self.sock.state != ns.NET_STATE_ESTABLISHED:
			self.startup()

	def set_dispatch(dispatch):
		self.dispatch = dispatch

	def set_ip(self, ip):
		self.ip = ip

	def set_port(self, port):
		self.port = port

	def set_hid(self, hid):
		self.hid = hid

	def set_room(self, room):
		self.room = room

	def set_table(self, table):
		self.table = table

	def set_seat(self, seat):
		self.seat = seat

	def enter_game(self, room, table, seat):
		self.room = room
		self.table = table
		self.seat = seat
		jdata = {}
		jdata['tag'] = dtag.UPDATE_ROOM
		jdata['room'] = self.room
		jdata['table'] = self.table
		jdata['seat'] = self.seat
		self.send(json.dumps(jdata))

	def send(self, data):
		self.sock.send(data)

	def send_chat_msg(self, jdata):
		self.sock.send(json.dumps(jdata))

	def send_one_step(self, jdata):
		self.sock.send(json.dumps(jdata))

	def send_room_table(self, room, table, seat):
		jdata = {}
		jdata['tag'] = dtag.UPDATE_STATE
		jdata['room'] = room
		jdata['table'] = table
		jdata['seat'] = seat
		self.sock.send(json.dumps(jdata))

	def update_state(self, jdata):
		self.roomchat = jdata['msg']
		self.tables = jdata['rooms']

	def update_require(self):
		jdata = {}
		jdata['tag'] = dtag.UPDATE_STATE
		self.sock.send(json.dumps(jdata))

	def recv(self):
		self.sock.process()
		data = self.sock.recv()
		return data

	def close(self):
		jdata = {}
		jdata['tag'] = dtag.CLOSE_CLIENT
		jdata['hid'] = self.hid
		self.sock.send(json.dumps(jdata))
		self.shutdown = True
		self.sock.close()

#----------------------------------------------------------------------
# testing case
#----------------------------------------------------------------------
if __name__ == '__main__':
	client = GomokuClient()
	client.set_room(2)
	client.set_table(3)
	client.startup()
	# client.process()
	client.send_room_table( 1, 2, 1)
	t1 = threading.Thread(target=client.process)
	t1.start()

	client.send_chat_msg("中文信息 message")
	# client.close()