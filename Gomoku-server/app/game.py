#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# game.py
#                                                                                                                                                                     
#======================================================================
import sys
sys.path.append("..")
import lib.log as log

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

logger = log.get_logger('GomokuGame')
#======================================================================
# 服务端主类
#======================================================================
class GomokuGame(object):
	"""docstring for GomokuGame"""
	global logger
	def __init__(self):
		super(GomokuGame, self).__init__()

		self._init_attr()
		pass

    #----------------------------------------------------------------------
    # 类属性设置
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

	def _set_panel(self, flag, row, column):
		self.panel[row][column] = flag
		self.records.append((flag, row, column))

	def set_bplayer(self, hid):
		self.bplayer = hid

	def set_wplayer(self, hid):
		self.wplayer = hid

	# 重置游戏
	def reset_game(self):
		del self.records[0:len(self.records)]
		for row in xrange(self.rows):
			for column in xrange(self.columns):
				self.panel[row][column] = 0

    #----------------------------------------------------------------------
    # 游戏状态管理
    #----------------------------------------------------------------------

    # 下一步棋
	def play_one_step(self, uid, row, column):
		flag = BACK_FLAG
		if uid == self.wplayer:
			flag = WHITE_FLAG
		self._set_panel(flag, row, column)
		win = self.is_win(flag, row, column)
		return win

	# 判断游戏输赢
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

	# 悔棋
	def back_move(self):
		# 双方各回退一个棋子
		step = 1
		while step > 0:
			step -= 1
			flag, row, column = self.records.pop()
			self.panel[row][column] = 0