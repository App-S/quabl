from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.che.iitb.ac.in/online/people/viewstudents?filter0=**ALL**&op1=%3E%3D&filter1=2011"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td/a")
i=0
while 1:
	cl=browser.find_elements_by_xpath("//tbody/tr/td/a")
	for c in cl:
		i+=1
		if(i%2!=1):
			continue
		profile={}
		temp=c.text.strip()
		profile["name"]=temp
		data.append(profile)
		print i
		with open("chem.json","w") as f:
			json.dump(data,f)	
		if(i%40==39):
			print "wait"
			time.sleep(5)

