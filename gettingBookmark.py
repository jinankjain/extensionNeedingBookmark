#!/usr/local/bin/python
# coding: latin-1

import requests
from bs4 import BeautifulSoup
import urllib2

for pagenumber in range(2,21):
	url = 'https://crx.dam.io/pages/{}.html'.format(pagenumber)
	#url = 'https://crx.dam.io/'
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	
	fileName = "list.txt"
	print "List of Extension that uses Bookmark as a permission"
	listOfBookMark = open(fileName)
	for extension in listOfBookMark.read().split(','):
		extName = soup.findAll('h2', {"id": extension[2:-1]})
		if extName:
			print extName[0].find('a').contents