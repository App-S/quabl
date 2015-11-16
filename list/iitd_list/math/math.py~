from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="file:///home/harsha1397/Documents/quabl/iitd_list/math/3.htm"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_class_name("ppp")
for c in cl:
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("math3.json","w") as f:
	json.dump(data,f)	

