#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple keyword collection procedures '
__author__ = 'Leslie Wong'

import urllib.request
import re
import time
import linecache


word_num = 1

while True:
	word = linecache.getline('words.txt', word_num)
	print(word_num,':', word)
	word_num = word_num + 1
	# if word_num > 100000:
		# break
	time.sleep(1)
	linecache.clearcache()
	with open('words.txt', 'a') as f:
		word = urllib.request.quote(word)
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
		word_str = re.findall(r"\"s\":(.*)", html)
		new_words = re.findall(r"\"(.*?)\"", word_str[0])
		for new_word in new_words:
			f.write(new_word+'\n')
		time.sleep(1)
