from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.aero.iitb.ac.in/home/index.php?option=com_content&task=view&id=19&Itemid=27"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
k=browser.find_elements_by_class_name("thickbox")
i=0
for l in k:
	if(i<2):
		i+=1
		continue
	else:
		print l
		l.click()
		break
cl=browser.find_elements_by_xpath("//table/tbody/tr/td")
i=0
for c in cl:
	i+=1
	if(i%3!=0):
		continue
	profile={}
	profile["name"]=c.text.strip()
	data.append(profile)
	if(profile["name"]=="BHAVYA SENWAR"):
		break
with open("ae3.json","w") as f:
	json.dump(data,f)	

