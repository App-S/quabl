from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="https://www.cse.iitb.ac.in/page222?batch=PhD"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
s="row1"
cl=soup.find_all(class_=s)
for c in cl:
	profile={}
	temp=c.text.strip()
	profile["name"]=''
	for t in temp :
		if t in "abcdefghijklmnopqrstuvwxyz":
			break
		profile["name"]+=t
	data.append(profile)
s="row2"
cl=soup.find_all(class_=s)
for c in cl:
	profile={}
	temp=c.text.strip()
	profile["name"]=''
	for t in temp :
		if t in "abcdefghijklmnopqrstuvwxyz":
			break
		profile["name"]+=t
	data.append(profile)
with open("8.json","w") as f:
	json.dump(data,f)	

