#!/bin/python2.7
# coding=utf-8

import mysql.connector as mariadb
from config import Config


class Database():

	def __init__(self, database):
		cnf = Config()
		self.user = cnf.get_mysql_credentials()['username']
		self.password = cnf.get_mysql_credentials()['password']
		self.database = database

		self.mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
		self.cursor = self.mariadb_connection.cursor()
		if self.cursor is not None:
			return True


	def query(self, sql_stmt):
		try:
			self.cursor.execute(self.sql_stmt)
		except mariadb.Error as error:
			print("Error: {}".format(error))
		if cursor.with_rows:
			return cursor.fetchall()


	def close(self):
		self.mariadb_connection.close()
		
