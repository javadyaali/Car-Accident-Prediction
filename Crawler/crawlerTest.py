
# script to download content using various apis
# author : Appu Shaji ( contact me at appoose at gmail )
# license : GPLv3 
# date : 20th Feb 2013

import urllib
import sys
import time
import os
import requests
import getpass
import datetime
import simplejson
import re

your_develop_key = 'AIzaSyDvhivCsnsWI1RP7zoGKgsWqW9FytBCiW8'
your_engine_cx = '010888522299621574176:wkseuv8sezc'


class CrawlData():
	def __init__(self,searchEngine):
		self.searchEngine = searchEngine
		self.count = 0
		if searchEngine == 'google':
			self.baseDir = 'googleImageResults'
			self.rootUrl = 'https://www.googleapis.com/customsearch/v1?q='
			self.apiKey = 'AIzaSyDvhivCsnsWI1RP7zoGKgsWqW9FytBCiW8' # not needed if want < 64 images. Have not implemented the paid account version
			self.opUrlKey = 'unescapedUrl'


	def grabData(self,dataInfo):
		for j in range(len(dataInfo)):
			currUrl = dataInfo[j][self.opUrlKey]
			opFileName = '{0}/Image_{1:010d}.jpg'.format(self.opDir,self.count)
			print opFileName
			urllib.urlretrieve(currUrl,opFileName)
			self.count = self.count + 1

	def doSearch(self,queryTerm,pageNumber):

		self.opDir = self.baseDir + '/' + queryTerm
		if not os.path.exists(self.opDir):
			os.makedirs(self.opDir)
	
		if self.searchEngine == 'google':
			searchUrl = self.rootUrl + urllib.quote(queryTerm) +'&start='+str(pageNumber*8)+'&userip=MyIP&rsz=8&imgtype=photo'
			print searchUrl
			try:
				response = requests.get(searchUrl).json()
				dataInfo = response['responseData']['results']
			except (IndexError,TypeError,ValueError,NameError):  
				print 'skipping'
				return 

		
		self.grabData(dataInfo)
		


def searchImage(searchTerm,searchEngine):
	currSearch = CrawlData(searchEngine)
	numPages = 10	
	for i in range(numPages):
		currSearch.doSearch(searchTerm,i)
		time.sleep(0.5) # for throttling

def searchPopular(searchEngine):
	currPopularSearch = CrawlData(searchEngine)
	numPages = 3000
	for i in range(numPages):
		currPopularSearch.doSearchPopular(i)



if __name__ == '__main__':
	print len(sys.argv)
	if len(sys.argv) > 2:
		searchTerm = ''
		if sys.argv[len(sys.argv)-1] == 'google':
			searchEngine = sys.argv[len(sys.argv)-1]
			searchQueryRange = len(sys.argv)-1			
		else:
			print 'using default search engine'
			searchEngine = 'google' # default one
			searchQueryRange = len(sys.argv)
		for i in range(1,searchQueryRange):
			searchTerm = searchTerm + sys.argv[i] + " "
	elif len(sys.argv) == 2:
		print sys.argv[1]
		searchTerm = sys.argv[1]
	else: 
		print 'OH OH'
		searchEngine = 'google'
		searchTerm = 'car accident'

	searchImage(searchTerm.strip(),searchEngine)

