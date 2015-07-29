#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

#======================================================================
# logger日志
#======================================================================

def get_logger(owner):
	logger = logging.getLogger(owner)
	logger.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# 定义handler的输出格式  
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	return logger