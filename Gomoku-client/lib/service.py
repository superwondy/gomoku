#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class service(object):
	"""docstring for service"""
	def __init__(self):
		super(service, self).__init__()
		self.SID = random.randint(10000, 40000)
		self._command_map = {}
		# print 'SID=' + str(self.SID)

	def set_sid(self, sid):
		self.service_id = sid

	def handle(self, msg, owner):
		cid = msg['tag']
		if not cid in self._command_map:
			raise Exception('bad command %s' % cid)
		f = self._command_map[cid]
		return f(msg)

	def register(self, cid, func):
		self._command_map[cid] = func

	def registers(self, CommnadDict):
		self._command_map = {}
		for cid in CommnadDict:
			print 'cid=' + str(cid)
			self.register(cid, CommnadDict[cid])
		return 0
