from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://mech.iitd.ac.in/onroll/pg/MTECH/MTECH%20INDUSTRIAL%20ENGINEERING"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
while 1:
	cl=browser.find_elements_by_xpath("//tbody/tr/td")	
	for c in cl:
		profile={}
		temp=c.text.strip()
		if temp.startswith('2'):
			continue
		profile["name"]=temp
		data.append(profile)
	print "4 sec"
	time.sleep(4)
	print"scanning"
	with open("pg3.json","w") as f:
		json.dump(data,f)	

