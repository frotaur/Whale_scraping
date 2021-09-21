from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome("chromedriver")

driver.get("https://www.google.com/search?q=whale&tbm=isch&ved\
	=2ahUKEwipntyzkpDzAhUX8IUKHRyYCgwQ2-cCegQIABAA&oq=whale&gs_\
	lcp=CgNpbWcQA1AAWABg1wxoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6\
	LWltZw&sclient=img&ei=P9pJYemCLZfglwScsKpg&bih=1057&biw=1920")

time.sleep(2)
scroll_pause = 1
screen_height = driver.execute_script("return window.screen.height;")
i=1
scroll_max=10

while True:
	driver.execute_script("window.scrollTo(0,{screen_h}*{i});".format(screen_h=screen_height,i=i))
	i+=1
	time.sleep(scroll_pause)
	scroll_height = driver.execute_script("return document.body.scrollHeight;")
	if (screen_height * i > scroll_height or i> scroll_max):
		break  

img_urls = []

driver.close()