from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import pickle

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.get("https://yandex.com/images/search?text=whale")
actionman = ActionChains(driver)

time.sleep(10)
scroll_pause = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1
scroll_max = 10
last_height = driver.execute_script("return document.body.scrollHeight")

while i < scroll_max:
	# Scroll down to bottom
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# Wait to load page
	time.sleep(scroll_pause)

	# Calculate new scroll height and compare with last scroll height
	new_height = driver.execute_script("return document.body.scrollHeight")

	if new_height == last_height:
		# We reached the end
		break

	last_height = new_height
	i += 1

time.sleep(10)

image_links = driver.find_elements_by_class_name("serp-item__link")

actionman.move_to_element(image_links[0]).perform()
image_links[0].click()
time.sleep(1)


url_tab = []
ended = False
while not ended:
	time.sleep(2)
	url_temp = driver.find_elements_by_class_name("MMImage-Origin")
	print(url_temp[0].get_attribute("src"))
	url_temp[0].click()
	if(url_tab):
		if(url_tab[-1] == url_temp[0].get_attribute("src")):
			ended = True
	url_tab.append(url_temp[0].get_attribute("src"))



with open("whale-url.pkl", "wb") as f:
	pickle.dump(url_tab, f)

driver.close()
driver.quit()
