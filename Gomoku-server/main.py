#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from app.mainserver import MainServer

#----------------------------------------------------------------------
# testing case
#----------------------------------------------------------------------
if __name__ == '__main__':
	server = MainServer()
	server.startup()
	server.process()