from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.hss.iitb.ac.in/en/mphil-0"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td")
i=0
for c in cl:
	i+=1
	if(i%3!=0):
		continue
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("mphil.json","w") as f:
	json.dump(data,f)	

