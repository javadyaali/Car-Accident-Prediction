import json 
import os
import sys
import requests

def urlGenerator(queryCount):
	urlList = []
	for i in range(1,queryCount+1):
		url = "https://pixabay.com/api/?key=9471200-777aae0fd082c8540588f4f32&q=car+accident&image_type=photo&page="+str(i)+"&per_page=200"
		urlList.append(url)
	return urlList

def getRequest(url):
	response = requests.get(url)
	return response.text


def makeJson(response):
	jsonData = json.loads(response)

	return jsonData

def extractLinks(jsonData):
	output = []
	for item in jsonData["hits"]:
		output.append(item["fullHDURL"])
	return output

def download(links, index):
	subscript  = ".jpg"
	for item in links:

		try:
		    os.system('wget --tries=1 --read-timeout=5 ' + '\''+item+'\'' + ' -O \'./image/' + 'car-accident' + '/'+ str(index) + subscript + '\'')
		    index += 1
		except:
			print('Save error!')
	return index
