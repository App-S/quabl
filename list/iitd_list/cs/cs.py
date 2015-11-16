from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://cse.iitd.ac.in/index.php/2011-12-29-23-14-30/students?id=97"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td/a")
for c in cl:
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("m14.json","w") as f:
	json.dump(data,f)	

