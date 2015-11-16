from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.civil.iitb.ac.in/students.php?sort=Phd&courseType=5"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//h4")
i=0
for c in cl:
	i+=1
	profile={}
	profile["name"]=c.text.strip()
	data.append(profile)
with open("phd.json","w") as f:
	json.dump(data,f)	

