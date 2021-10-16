import requests
from bs4 import BeautifulSoup

# alllinks = [str("https://www.gettyimages.fr/photos/whale-photo-underwater?assettype=image&phrase=whale%20photo"+"%"+
# 	"20underwater&sort=mostpopular&license=rf%2Crm&page="+str(i))for i in range(1,101)]
# i=0
# pagenum=1
# for link in alllinks:
# 	page = requests.get(link)
# 	print(page.status_code)
# 	soup = BeautifulSoup(page.content,"html.parser")

# 	pics=soup.find_all('picture')
# 	print(pics)
# 	print(list(pics)[0].prettify())
# 	urltab = []

# 	for pic in pics :
# 		sor = pic.find("source")
# 		urltab.append(sor["srcset"])

# 	for url in urltab :
# 		img = requests.get(url)
# 		file = open("GettyWhales/"+str(i)+".png","wb")
# 		file.write(img.content)
# 		file.close()
		
# 		i+=1
# 	print("pagenum : ", pagenum)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import pickle

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
allinks = ["https://www.gettyimages.fr/photos/whale-photo-underwater?assettype=image&phrase=whale%20photo"+"%"+
	"20underwater&sort=mostpopular&license=rf%2Crm&page={}".format(i) for i in range(1,21)]
img_urls = []
print("I HATE YOU, I HATE YOU !!!!")
for link in allinks:
	driver.get(link)

	time.sleep(2)

	
	image_links = driver.find_elements_by_class_name("MosaicAsset-module__thumb___YJI_C")
	for imag in image_links:
		print("newlink  : {}".format(imag.get_attribute("src")))
		img_urls.append(imag.get_attribute("src"))


with open('getty-url.pkl', 'wb') as file:
	pickle.dump(img_urls,file)
	file.close()

driver.close()
driver.quit()