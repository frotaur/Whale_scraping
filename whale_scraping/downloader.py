import pickle
import requests


url_tab = []


# Load whale urls
with open('istock-url.pkl', 'rb') as file:

	# A new file will be created
	url_tab = pickle.load(file)
	file.close()

i = 0
print(len(url_tab))
bad_urls = []

for url in url_tab:
	try:
		resp = requests.get(str(url))
	except Exception:
		continue
	try:
		imgformat = resp.headers["Content-Type"]
	except KeyError:
		print("no type found, assuming jpg")
		imgformat="image/jpeg"

	goodformat=True
	if imgformat not in {"image/png","image/jpeg", "image/gif","image/jpg"}:
		print("Content type {} not supported".format(imgformat))
		goodformat=False
	print(url)
	if(goodformat):
		with open("Whales_istock/whale_{i}.{imgform}".format(i=i,imgform=imgformat[6:]),"wb") as image:
			image.write(resp.content)
			image.close()
	else:
		bad_urls.append(url)
	i+=1

with open("bad_urls_istock.pkl","wb") as file:
	pickle.dump(bad_urls,file)
	file.close()
