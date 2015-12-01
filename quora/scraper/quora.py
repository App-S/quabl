from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json

def x(a=[0]):
    a[0] += 1
    print "counter"
    print a    

def find_class(classname,name,soup,data):
    x=soup.find(class_=classname)
    if x:
        data[name]=x.text.strip().encode("utf-8").decode('unicode_escape').encode('ascii','ignore')
    if(name=='Questions Asked'):
    	data[name]=data[name][9:]
    	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    if(name=='Followers'):
    	data[name]=data[name][10:]
    	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    if(name=='Following'):
    	data[name]=data[name][10:]
    	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    if(name=='Edits'):
    	data[name]=data[name][5:]
       	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    if(name=='Questions Answered'):
    	data[name]=data[name][7:]
       	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    if(name=='Posts'):
    	data[name]=data[name][5:]
     	tmp=''
    	for t in data[name]:
		if t.isdigit():
			tmp+=t
	data[name]=tmp
    
def find_all_class(classname,name,soup,data):
    x=soup.find_all(class_=classname)
    data[name]=""
    if x:
    	w=0
    	temp=''
    	temp2=''
    	if(name=='About'):
		for y in x:
			if w==1:
				data[name]+='<delimit>'
			if w!=1:
				if w==2 :
					temp2=y.text.strip().encode("utf-8").decode('unicode_escape').encode('ascii','ignore').strip()
				if w==0 :
					data[name]=y.text.strip().encode("utf-8").decode('unicode_escape').encode('ascii','ignore').strip()
			else:
				temp=y.text.strip().encode("utf-8").decode('unicode_escape').encode('ascii','ignore').strip()
			#data[name]=data[name].strip()
			w+=1
		if(w==2):
			data[name]+='NA<delimit>'+temp
		if(w==3):
			data[name]+=temp+'<delimit>'+temp2
		if(w==1):
			data[name]+='<delimit>NA<delimit>NA'
	else:
		for y in x:
			if(w!=0):
				data[name]+='<delimit>'
			temp=y.text.strip().encode("utf-8").decode('unicode_escape').encode('ascii','ignore').strip()
			tmp=[]
			tmp=temp.split('Answers',1)
			if len(tmp)==1:
				tmp=tmp+['NA']
			tmp1=''
			if(tmp[1]!='NA'):
				for t in tmp[1]:
					if t.isdigit():
						tmp1+=t
					else:
						break
				tmp[1]=tmp1
				#print'tmp1'
				#print tmp1
			data[name]+=tmp[0]+'<delimit>'+tmp[1]
			w+=1
		if(w==0):
			data[name]='NA<delimit>NA<delimit>NA<delimit>NA<delimit>NA<delimit>NA'
		elif(w==1):
			data[name]+='<delimit>NA<delimit>NA<delimit>NA<delimit>NA'
		elif(w==2):
			data[name]+='<delimit>NA<delimit>NA'
def find_id(iid,name,soup,data):
	x=soup.find(id=iid)
	if x:
		data[name]=x.text.strip()

def find_tag(tag,name,soup,data):
	x=soup.find(tag)
	if x:
		data[name]=x.text.strip()
		
def parse_page(soup,data):
	find_tag('h1','Name',soup,data)
	find_class('ProfileBio','Profile Bio',soup,data)
	find_class('IdentitySig UserSig','Short Bio',soup,data)
	find_class('EditableListItem QuestionsNavItem NavItem NavListItem not_removable','Questions Asked',soup,data)
	find_class('EditableListItem NavListItem NavItem AnswersNavItem not_removable','Questions Answered',soup,data)
	find_class('EditableListItem NavListItem PostsNavItem NavItem not_removable','Posts',soup,data)
	find_class('EditableListItem NavListItem FollowersNavItem NavItem not_removable','Followers',soup,data)
	find_class('FollowingNavItem NavListItem NavItem EditableListItem not_removable','Following',soup,data)
	find_class('OperationsNavItem NavListItem NavItem EditableListItem not_removable','Edits',soup,data)
	find_all_class('EditableListItem ProfileExperienceItem is_removable','Knows About',soup,data)
	find_all_class('EditableListItem ProfileAboutItem is_removable','About',soup,data)
	
	x=soup.find(class_='Profile ActionBar')
	if x:	
		y=x.find_all(class_='action_item')
		if y:
			w=0
			for z in y:
				w+=1
				if(w<3):
					continue
				link=z.find('a',href=True)
				data[z.text]=link['href']
    
def contains(string,sub):
    return string.find(sub)>=0

def parse(html):
    soup=bs(html);
    data={}
    parse_page(soup,data)
    #if 'About' in data:
        #name=data['About']
        #if(contains(name,'IIT') or contains(name,'Indian Institute of Technology')or contains(name,'Birla') or contains(name,'IIM')):
    x()
    #dt=clean(data)
    return data
    #return ''

def clean(data):
	s=''
	if('Name' in data):
		s+=data['Name']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Questions Asked' in data):
		s+=data['Questions Asked']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Questions Answered' in data):
		s+=data['Questions Answered']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Posts' in data):
		s+=data['Posts']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Followers' in data):
		s+=data['Followers']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Following' in data):
		s+=data['Following']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Edits' in data):
		s+=data['Edits']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('url' in data):
		s+=data['url']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Twitter' in data):
		s+=data['Twitter']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('LinkedIn' in data):
		s+=data['LinkedIn']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Facebook' in data):
		s+=data['Facebook']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Profile Bio' in data):
		s+=data['Profile Bio']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Short Bio' in data):
		s+=data['Short Bio']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('About' in data):
		if(data['About']==''):
			data['About']='NA<delimit>NA<delimit>NA'
		s+=data['About']+'<delimit>'
	else:
		s+='NA<delimit>'
	if('Knows About' in data):
		if(data['Knows About']==''):
			data['Knows About']='NA<delimit>NA<delimit>NA<delimit>NA<delimit>NA<delimit>NA'
		s+=data['Knows About']
	else:
		s+='NA'
	return s


def get_data(browser):
    browser.get(url)
    return parse(browser.page_source)
    
def get_quora_data(lurl,browser):
	print lurl
	browser.get(lurl)
	parse_data=parse(browser.page_source)
	parse_data['url'] = lurl
	pd=clean(parse_data)
	return pd

browser=webdriver.Firefox()
u='https://www.quora.com/profile/Anurag-Kumar-4'
#u="https://www.quora.com/profile/Akhyansh-Mohapatra"
data=get_quora_data(u,browser)
print data
