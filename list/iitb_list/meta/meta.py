from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.met.iitb.ac.in/main.html?s=y&sec=people&content=studentList/phd12a"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
i=0
print "W"
cl=browser.find_elements_by_xpath("//tbody/tr/td")
for c in cl:
	i+=1
	if(i%3!=2):
		continue
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
	with open("phd12.json","w") as f:
		json.dump(data,f)	

