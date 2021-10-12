from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import pickle

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
allinks = ["https://www.istockphoto.com/fr/search/2/image?mediatype=photography&phrase=whale%20underwater&sort=best&page={}".format(i) for i in range(1,101)]
img_urls = []

for link in allinks:
	driver.get(link)

	time.sleep(2)

	
	image_links = driver.find_elements_by_class_name("MosiacAsset-module__thumb___L2F4y")

	for imag in image_links:
		print("newlink  : {}".format(imag.get_attribute("src")))
		img_urls.append(imag.get_attribute("src"))


with open('istock-url.pkl', 'wb') as file:
	pickle.dump(img_urls,file)
	file.close()

driver.close()
driver.quit()
