# this crawler use https://pixabay.com/api/docs/
# my key = 9471200-777aae0fd082c8540588f4f32

from Downloader import *
import json 
import os
import sys
import requests


query = "car accident"
quaryCount = 50
index = 1


urlList = urlGenerator(quaryCount)

for url in urlList:

	response = getRequest(url)

	jsonData = makeJson(response)

	links = extractLinks(jsonData)

	index = download(links, index)

print("Done !!")