#!/usr/bin/env python
# -*- coding: utf-8 -*-

class dispatcher(object):
	"""docstring for dispatcher"""
	def __init__(self):
		super(dispatcher, self).__init__()
		self._service_map = {}

	def dispatch(self, msg, owner):
		sid = msg['sid']
		if not sid in self._service_map:
			raise Exception('bad service %d' % sid)
		svc = self._service_map[sid]
		svc.handle(msg, owner)

	def register(self, sid, svc):
		self._service_map[sid] = svc