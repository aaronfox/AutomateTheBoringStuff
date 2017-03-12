#! python3
#
# imgurPhotos.py - opens the first five pictures of a searcch on imgur

import requests, sys, webbrowser, bs4, pyperclip

headerInfo = {"User-Agent": "Mozilla/5.0"}

searchQuery = ''
if len(sys.argv) > 1:
    searchQuery = ' '.join(sys.argv[1:])
else:
    searchQuery = pyperclip.paste()
res = requests.get('https://imgur.com/search?q=' + searchQuery, headers = headerInfo)
res.raise_for_status()

# obtain first few images
imageSoup = bs4.BeautifulSoup(res.text, 'html.parser')

imageElems = imageSoup.select('.image-list-link')

amtToOpen = min(5, len(imageElems))
for i in range(amtToOpen):
    imagehref = imageElems[i].get('href')
    webbrowser.open('https://imgur.com/' + imagehref)
