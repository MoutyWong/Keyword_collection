#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' init database '
__author__ = 'Leslie Wong'


import urllib.request
import re
import time
import linecache
import mysql.connector


conn = mysql.connector.connect(user='root', password='password', database='words')
cursor = conn.cursor()
with open('words.txt', 'r') as f:
	for line in f:
		print(line)
		cursor.execute('insert into words (word) values (%s)', [line])
		cursor.rowcount
conn.commit()
cursor.close()
conn.close()
		