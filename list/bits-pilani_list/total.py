from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="file:///home/harsha1397/Desktop/priority_nos.htm"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_class_name("p1ft0")
for c in cl:
	profile={}
	profile["name"]=c.text.strip()
	data.append(profile)
with open("total.json","w") as f:
	json.dump(data,f)	

