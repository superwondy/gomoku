#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# clientgame.py - network data stream operation interface
#
#                                                                                                                                                                        
#======================================================================
import logging

#======================================================================
# format of headers
#======================================================================
BACK_FLAG = 1
WHITE_FLAG = 2
WIN_COUNT = 5

LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1


logger = logging.getLogger('ClientGame')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class ClientGame(object):
	"""docstring for ClientGame"""
	def __init__(self):
		super(ClientGame, self).__init__()

		self._init_attr()
		pass

	#----------------------------------------------------------------------
	# initial gomoku game attribute
	# record: a list with tuple(player, row, column)
	# bplayer, wplayer, the players' uid(hid)
	#----------------------------------------------------------------------
	def _init_attr(self):
		self.rows = 15
		self.columns = 15
		self.panel = [[0 for col in range(self.columns)] for row in range(self.rows)]
		self.records = []
		self.bplayer = None
		self.wplayer = None
		self.room = None
		self.table = None
		pass

	def _set_panel(self, flag, row, column):
		self.panel[row][column] = flag
		self.records.append((flag, row, column))
		pass

	def play_one_step(self, uid, row, column):
		flag = BACK_FLAG
		if uid == self.wplayer:
			flag = WHITE_FLAG
		self._set_panel(flag, row, column)
		win = self.is_win(flag, row, column)
		return win

	def is_win(self, flag, row, column):
		#向左
		count = 1
		count = self.count_flag(flag, row, column, LEFT, 0, count)
		if count >= WIN_COUNT:
			return True
		#向右
		count = self.count_flag(flag, row, column, RIGHT, 0, count)
		if count >= WIN_COUNT:
			return True

		#向上
		count = 1
		count = self.count_flag(flag, row, column, 0, UP, count)
		if count >= WIN_COUNT:
			return True
		#向下
		count = self.count_flag(flag, row, column, 0, DOWN, count)
		if count >= WIN_COUNT:
			return True

		#左上角
		count = 1
		count = self.count_flag(flag, row, column, LEFT, UP, count)
		if count >= WIN_COUNT:
			return True
		#右下角
		count = self.count_flag(flag, row, column, RIGHT, DOWN, count)
		if count >= WIN_COUNT:
			return True

		#右上角
		count = 1
		count = self.count_flag(flag, row, column, RIGHT, UP, count)
		if count >= WIN_COUNT:
			return True
		#左下角
		count = self.count_flag(flag, row, column, LEFT, DOWN, count)
		if count >= WIN_COUNT:
			return True
		return False

	def count_flag(self, flag, row, column, move_x, move_y, count):
		c_r = row + move_x
		c_c = column + move_y
		while c_r >= 0 and c_r < self.rows and c_c >= 0 and c_c < self.columns and self.panel[c_r][c_c] == flag:
			count += 1
			c_r += move_x
			c_c += move_y
		return count


	def _back_move(self):
		record = self.records.pop()
		logger.debug('back move: ' + str(record))
		return record
