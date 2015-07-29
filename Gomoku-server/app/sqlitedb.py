 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class SqliteDb(object):
	"""docstring for SqliteDb"""
	def __init__(self, db=None, table=None):
		super(SqliteDb, self).__init__()

		if not db:
			self.db = 'data.db'
			self.table = 'user_info'
		else:
			self.db = db
			self.table = table

		try:
			self.conn = sqlite3.connect(self.db)
			self.cursor = self.conn.cursor()
			self._init_table()
		except sqlite3.Error, e:
			if self.conn:
				self.conn.rollback()
		finally:
			pass

	def _init_table(self):
		self.create_table()
		self.insert_db('user1')
		self.insert_db('user2', 10)

	def create_table(self):
		with self.conn:
			sql = 'create table if not exists ' + self.table \
			+ '''('id' INTEGER PRIMARY KEY AUTOINCREMENT, Name CHAR(32), Score INTEGER)'''
			self.cursor.execute(sql)
			self.conn.commit()


	def select_by_name(self, name):
		with self.conn:
			sql = 'select * from ' + self.table \
			+ ''' WHERE Name = '%s' LIMIT 1''' % (name)
			self.cursor.execute(sql)
			result = self.cursor.fetchone()
			return result

	def insert_db(self, name, score=0):
		with self.conn:
			sql = 'insert into ' + self.table + '''(Name, Score) values ('%s', %d)''' % (name, score)
			self.cursor.execute(sql)
			self.conn.commit()

	def update_score(self, name, score):
		with self.conn:
			sql = 'update ' + self.table + '''set Score = %d where Name = '%s' ''' % (score, name)
			self.cursor.execute(sql)
			self.conn.commit()

	def select_all(self):
		with self.conn:
			sql = 'select * from ' + self.table
			self.cursor.execute(sql)
			resl = []
			result = self.conn.fetchone()
			while result:
				resl.append(result)
				result = self.conn.fetchone()

	def close(self):
		self.cursor.close()
		self.conn.close()