from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://civil.iitd.ac.in/index.php?lmenuid=phd"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td/b")
for c in cl:
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("phd.json","w") as f:
	json.dump(data,f)	

