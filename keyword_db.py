#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' keyword2db'

__author__ = 'Leslie Wong'

import urllib.request
import re
import time
import linecache
import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='words')
# cursor = conn.cursor()

word_id = 1
while True:
	cursor = conn.cursor()
	cursor.execute('select word from words where id = %s', (word_id,))
	values = cursor.fetchall()
	print(word_id, values[0][0])
	cursor.close()
	word_id = word_id + 1
	if word_id >10:
		break
		
	word = urllib.request.quote(values[0][0])
	url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd='+ word+'&json=1&p=3&sid=18285_1444_17758_19671_19781_19806_19900_19558_19808_19842_19901_19860_15733_11535&req=2&csor=8&pwd=&cb=jQuery110208427646549311438_1462241281514&_=1462241281525'
	headers = {
		'GET': url,
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Host': 'sp0.baidu.com',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
	}
	
	req = urllib.request.Request(url)
	for key in headers.keys():
		req.add_header(key, headers[key])
	html = urllib.request.urlopen(req).read().decode('gbk')
	word_str = re.findall(r'\"s\":(.*)', html)
	new_words = re.findall(r'\"(.*?)\"', word_str[0])
	
	cursor = conn.cursor()
	for new_word in new_words:
		cursor.execute('insert into words (word) values (%s)', [new_word])
	conn.commit()
	cursor.close()
	time.sleep(1)
conn.close()
