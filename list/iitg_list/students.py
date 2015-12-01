from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
#url="http://www.iitg.ac.in/biotech/Students.html"
url= raw_input('enter url ') 
filename=raw_input('enter filename ')+'.json'
dept= raw_input('enter dept. ') 
browser=webdriver.Firefox()
browser.get(url)
data=[]
#cl=browser.find_elements_by_xpath("//h3")
i=0
scrape=raw_input('scrape? ')
while(1):
	if(scrape!='y'):
		break 
	soup=bs(browser.page_source)
	cl=browser.find_elements_by_xpath("//tbody/tr/td")
	#cl=browser.find_elements_by_xpath("//h4")
	for c in cl:
		i+=1
		'''if(i%3!=0):
			continue'''
		profile={}
		temp=c.text.strip()
		if temp=='':
			continue
		if temp.startswith('Dr.'):
			continue
		if temp[0] in '\n0123456789qwertyuiopasdfghjklzxcvbnm':
			continue
		temp=temp.split('\n',1)[0]
		profile["name"]=temp
		profile['dept']=dept
		data.append(profile)
	scrape=raw_input('scrape? ')
with open(filename,"w") as f:
	json.dump(data,f)	

