# __author__=   'Sargam Modak'

import os
import json
import urllib2
import argparse
from bs4 import BeautifulSoup
from PIL import Image

"""
This link you can create according to your own requirement.
Search for the tag using http://www.google.co.in/search?q=your_tag
Then select the options like size you want etc. in tools option
copy the tbs="whatever is here" from the url and copy that to below url
For me the minimum size of the images I am searching are 400x300
"""
BASE_URL = 'http://www.google.co.in/search?q={}&tbm=isch&tbs=isz:lt,islt:qsvga'
HEADER = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/43.0.2357.134 " "Safari/537.36"}


def download_images(q, save_path):
	if not os.path.exists(save_path):
		os.makedirs(save_path)  # create directory for downloading the file
	url = BASE_URL.format(q)
	req = urllib2.Request(url=url,
	                      headers=HEADER)
	url_open = urllib2.urlopen(url=req)
	soup = BeautifulSoup(url_open,
	                     'html.parser')
	links = []
	for a in soup.find_all("div", {"class": "rg_meta"}):    # this is class of the div under which all the information
															# related to the image is stored
		text = json.loads(a.text)
		if text['ity'] in ['jpg', 'JPG']:
			link = text['ou']   # this tag contains the link of the image
			links.append(link)
	# print len(links)
	# print links
	i = 1
	for link in links:
		path = os.path.join(save_path, str(i)+'.jpg')
		try:
			req = urllib2.Request(link,
			                      headers=HEADER)
			raw_img = urllib2.urlopen(req).read()
			with open(path, 'wb') as f:
				f.write(raw_img)
				f.close()
			Image.open(path)    # save the image only when it is downloadable and after downloading is not corrupted
			i += 1  # if any error occured while saving the value of i does not change so next image overwrites the
					# current image
		except Exception as e:
			print "{} cannot be opened.".format(link)
			print e
			continue
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-q',
	                    '--query',
	                    help='keyword to be searched',
	                    type=str,
	                    required=True)
	args = vars(parser.parse_args())
	query = str(args['query'])
	query = query.replace('_', '%20')   # space will break the url so you need to pass your query with _ wherever you
										#  wnat space like for searching black pearl you have to pass black_pearl
	download_images(q=query,
	                save_path=os.path.join(".", "download", query))
