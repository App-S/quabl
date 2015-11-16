from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.ese.iitb.ac.in/student/157"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//td/div/span/a")
i=0
for c in cl:
	i+=1
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("btech13.json","w") as f:
	json.dump(data,f)	

