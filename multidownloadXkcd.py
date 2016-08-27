#! /usr/bin/python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading

url = 'http://xkcd.com/'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
	# Download the page.
	print('Downloading page %s%s...' % url, urlNumber)
	res = requests.get(url + urlNumber)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")
	
	# Find the URL of the comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
            print('Could not find comic image.')
	else:
            try:
            	comicUrl = 'http:' + comicElem[0].get('src')
		# Download the image.
		print('Downloading image %s...' % (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

            except requests.exception.MissingSchema:
            	# Skip the comic
        	continue

		# Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl))\
                                 , 'wb')
		for chunk in res.iter_content(100000):
		    imageFile.write(chunk)
		imageFile.close()

# Create and start the Thread objects
downloadThreads = []
objects
for i in range (0, 1400, 100): # loops 15 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
