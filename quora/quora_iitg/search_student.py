import quora_scrape
from selenium import webdriver
import json
import time
i=int(raw_input("enter last file no. "))
j=0
flag=0
def search(name,dept,browser):
	global j
	global i
	global flag
	j+=1
	'''if j<=237+469+91+741+119:
		return []'''
	if name=='Abhra Sarkar':
		flag=1
	if flag==0:
 		return []	
	profiles_list=[]
	iit=' Indian Institute of Technology, Guwahati'
	link="https://www.quora.com/search?q="+name+iit+"&type=profile"
	time.sleep(0.8)
	for profile in quora_scrape.get_quora_data(link,dept,browser):
		i=i+1
		stdinfo=str(i)+'.json'
		with open(stdinfo,'w') as f:
			f.write(profile)
		
	return profiles_list

def run_all(studentlist):
    browser=webdriver.Chrome()
    login = raw_input('Logged in to Quora? ')
    if login=='y':
        for student in studentlist:
            profiles=search(student['name'],student['dept'],browser)
            student['profiles']=profiles
            print 'got data for '+student['name']
        return studentlist

def contains(string,sub):
    return string.find(sub)>=0
	
def scrape_all():
    std_data=[];
    with open('iitg.json') as stdjson:
        std_data=json.load(stdjson)
    data_all= run_all(std_data)
scrape_all()
