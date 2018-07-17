# Api key = AIzaSyDvhivCsnsWI1RP7zoGKgsWqW9FytBCiW8
# Search engine ID = 010888522299621574176:wkseuv8sezc



#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" 
This is a simple command line tool to crawl images and save the result in local drive using google custom search api.
You should set you own search engine first. See README.md for help.
The code is based on google custom search sample.
"""

__author__ = 'spongezhang@gmail.com (Xu Zhang)'

import os
import sys
import pprint

from googleapiclient.discovery import build

#Pls set this before running the code. See README.md for help.
your_develop_key = 'AIzaSyDvhivCsnsWI1RP7zoGKgsWqW9FytBCiW8'
your_engine_cx = '010888522299621574176:wkseuv8sezc'

def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('customsearch', 'v1',
            developerKey="AIzaSyDvhivCsnsWI1RP7zoGKgsWqW9FytBCiW8")
  
    number_per_search = 10 #less than 10 for custom search engine, restricted by Google
    query = 'Car Accident'
    number_total = 100 #total number of image you want(less than 100, restricted by Google)

    try:
    	os.makedirs('./image/'+query)  
    except Exception,ex:
        print 'Directory existed'
    index = 0
    for group in range(0,int(number_total/number_per_search)):
        try:
            res = service.cse().list(
                q=query,
                cx = "010888522299621574176:wkseuv8sezc",
                num=number_per_search,
                searchType='image',
                start=group*10+1 #using different start index to get more search result
                ).execute()
            print res
        except Exception,ex:
            print 'Search Error!'
            
        for i in range(0,number_per_search):
            url = res['items'][i]['link']
            print(url)
            context_link = res['items'][i]['image']['contextLink']
            thumbnail_link = res['items'][i]['image']['thumbnailLink']
            subscript = '.jpeg'        
            if url.find('.gif')!=-1:
                subscript = '.gif'
            if url.find('.png')!=-1:
                subscript = '.png'
            if url.find('.tif')!=-1:
                subscript = '.tif'
            if url.find('.jpg')!=-1:
                subscript = '.jpg'            
            try:
                os.system('wget ' + '\''+url+'\'' + ' -O \'./image/' + query + '/'+ str(index)+subscript+'\'')
            except Exception,ex:
                print 'Save error!'
            index = index+1
            #show the search result 
            #pprint.pprint(res) 

if __name__ == '__main__':
    main()