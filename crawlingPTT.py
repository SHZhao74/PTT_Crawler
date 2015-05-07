# -*- coding: utf-8 -*-
#This is a PTT crawler
#I think it can become a tool which can help you buy something you chased in time.
#In the future, it will have a gui interface, and go into the page and pick its price up.
#If import bs4 occur ERROR, you should type "sudo easy-install BeautifulSoup4" on OSX.
#
#By Zhao Shou-Hao 2015.05.02 Taipei,Taiwan
import requests, time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'https://www.ptt.cc/bbs/HardwareSale/index2534.html'
wantStr = ['Ducky', '軸', 'filco']

def pickUpPrice(url):
	''' enter the item page and pick the price up
		2015.05.03
	'''
	res = requests.get('http://www.ptt.cc/' + url, verify = False)
	soup = BeautifulSoup(res.text)
	#print soup.text.split('◎欲售價格：')
	for  s in soup.find_all('span'):
		tmp = s.text
		#print type(tmp)


def craw():
	res = requests.get(url, verify = False)
	#content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(res.text)

	#print soup.select('a')
	for s in soup.select('.r-ent'):
		title = s.select('.title')[0].text
		for w in wantStr:
			if w in title:
				print s.select('.author')[0].text.strip() + title
				#pickUpPrice(soup)
				#print s
				tmp = str(s.find_all('a')[0])
				#print type(tmp)
				CostUrl = tmp.split('<a href="')[1].split('">')[0]
				pickUpPrice(CostUrl)
		else :
			pass


while 1:
	craw()
	print 'Sleep 5 min'
	time.sleep(60*5)