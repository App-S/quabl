import time
import quora_scrape
from selenium import webdriver
insti=raw_input("enter institute name without errors: ")
link="https://www.quora.com/search?q="+insti+"&type=profile"
i=int(raw_input("enter last file no.(or 0) "))
dept=raw_input('enter dept(or NA) ')
browser=webdriver.Chrome()
login = raw_input('Logged in to Quora? ')
if login=='y':
	browser.get(link)
	quora_scrape.get_quora_data(link,dept,browser,i)
