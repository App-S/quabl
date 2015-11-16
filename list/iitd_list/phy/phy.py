from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://physics.iitd.ac.in/content/onroll-msc-students"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td")
i=0
flag=0
for c in cl:	
	profile={}
	temp=c.text.strip()
	if temp.startswith('2'):
		continue
	if(temp=='ABHISHEK KUMAR'):
		flag=1
	if(flag==0):
		continue
	profile["name"]=temp
	data.append(profile)
with open("phy_msc.json","w") as f:
	json.dump(data,f)	

