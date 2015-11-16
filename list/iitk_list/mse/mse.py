from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.iitk.ac.in/mse/phd-students"
browser=webdriver.Chrome()
browser.get(url)
data=[]

#cl=browser.find_elements_by_xpath("//h3")
i=0
soup=bs(browser.page_source)
cl=browser.find_elements_by_xpath("//div/p")
for c in cl:
	profile={}
	temp=c.text.strip()
	'''if temp=='':
		continue
	if temp[0] in '123456789qwertyuiopasdfghjklzxcvbnm':
		continue'''
	
	profile["name"]=''	
	#profile["name"]=temp
	for t in temp:
		if t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
			profile["name"]+=t
		else:
			break
	data.append(profile)
with open("mse_phd.json","w") as f:
		json.dump(data,f)	

