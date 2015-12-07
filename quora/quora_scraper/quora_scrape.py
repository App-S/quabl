from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import quora
import time

def y(a=[0]):
    a[0] += 1
    print "total"
    print a  
def parse_page(url,browser,dept,soup,i):
	j=0
	browser2=webdriver.Chrome()
    login = raw_input('Logged in to Quora? ')
    if login=='y':
		while 1:
			soup=bs(browser.page_source)	
			p=soup.find(class_="QueryResultsList PagedList")
			profiles=soup.find_all(class_='pagedlist_item')
			for profile in profiles:
				if(j<i):
					j+=1
					continue
				j+=1
				time.sleep(0.8)
				l=profile.find('a')
				link=l['href']
				u='https://www.quora.com'+link
				data={}
				data=quora.get_quora_data(u,dept,browser2)	
				i=i+1
				stdinfo=str(i)+'.json'
				with open(stdinfo,'w') as f:
					f.write(data)
			j=0
			elem = browser.find_element_by_tag_name("body")
			elem.send_keys(Keys.PAGE_DOWN)
def parse(url,browser,dept,html,i):
	#html=browser.page_source
	soup=bs(html)
	data={}
	return parse_page(url,browser,dept,soup,i)


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
    
def get_quora_data(lurl,dept,browser,i):
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
   		return parse(lurl,browser,dept,browser.page_source,i)
   # except :
   		print 'error at url '+lurl
