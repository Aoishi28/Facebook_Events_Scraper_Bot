from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

user_id='your email id'
password='password'

chrome_browser= webdriver.Chrome(executable_path=r'C:\Users\Suprakash\Anaconda3\chromedriver', options=chrome_options)
chrome_browser.get('https://www.facebook.com/events?source=46&action_history=null')

time.sleep(1)

user_box = chrome_browser.find_element_by_xpath('//*[@id="email"]')       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box 

password_box = chrome_browser.find_element_by_xpath('//*[@id="pass"]')    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

password_box.send_keys(Keys.ENTER)

time.sleep(5)
pg=chrome_browser.page_source
soup=BeautifulSoup(pg,'lxml')
de=soup.findAll('div',{'class':"ck3b4tlb qlyowdya ehbs6d9j wp3ta8j8 mras6tbi dlbaxph7 t9u6kdq2 kkf49tns bi6gxh9e cgat1ltu aov4n071"}) #Since event details are in this class
de=de[:10] #Extracting the top 10 events
c=1 
for i in de:
	print("Event {}".format(c))
	info=i.findAll('div',{'class':"qzhwtbm6 knvmm38d"}) #Extracting the information about each event
	for i in info:
		print(i.text)
	c=c+1
	print("---------------------------------------------------")

chrome_browser.quit()