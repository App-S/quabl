from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import quora
import time

def y(a=[0]):
    a[0] += 1
    print "total"
    print a  
def parse_page(browser,dept,soup):
	list_u = []
	p=soup.find(class_="QueryResultsList PagedList")
	profiles=soup.find_all(class_='pagedlist_item')
	for profile in profiles:
	    time.sleep(0.8)
	    l=profile.find('a')
	    link=l['href']
	    u='https://www.quora.com'+link
	    data=quora.get_quora_data(u,dept,browser)
	    if(data):
	    	list_u.append(data)
	return list_u
def parse(browser,dept,url):
	html=browser.page_source
	soup=bs(html)
	data={}
	return parse_page(browser,dept,soup)


import requests 
import socket
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def get_data(browser):
    browser.get(url)
    return parse(browser,browser.page_source)
    
def get_quora_data(lurl,dept,browser):
   # try:
   		print lurl
		while(1):
			stat = is_connected()
			if stat==True :
				print "Status connected\n"				
				break
			print "No internet connection\n"
			time.sleep(1)	
   		browser.get(lurl)
   		y()
   		return parse(browser,dept,browser.page_source)
   # except :
   		print 'error at url '+lurl
