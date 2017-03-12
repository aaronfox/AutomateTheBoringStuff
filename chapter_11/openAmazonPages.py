#! python3
#
# openAmazonPages.py - opens the first five amazon product pages of a product
# that is input either by the command line or by the clipboard

# TODO: remove loggings

import requests, sys, webbrowser, bs4, logging, pyperclip

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

headerInfo = { "User-Agent": "Mozilla/5.0"}

headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
              "Accept-Encoding": "gzip, deflate, sdch, br", 
              "Accept-Language": "en-US,en;q=0.8", 
              "Host": "httpbin.org", 
              "Upgrade-Insecure-Requests": "1", 
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }

if len(sys.argv) > 1:
    res = requests.get('https://www.amazon.com/' +
        's/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
        + ' '.join(sys.argv[1:]), headers = headerInfo )
else:
    res = requests.get('https://www.amazon.com/' +
            's/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
            + pyperclip.paste(), headers = headerInfo )
res.raise_for_status()

# retrieve top product links
productSoup = bs4.BeautifulSoup(res.text)

# open a browser tab for each result
productElems = productSoup.select('.a-link-normal.s-access-detail-page.a-text-normal')
numOpen = min(5, len(productElems))

incrementer = 0
while incrementer < numOpen:
    if productElems[incrementer].get('href')[:3] != 'htt':
        incrementer += 1
        numOpen += 1
        continue
    incrementer += 1
    webbrowser.open(productElems[incrementer].get('href'))
    logging.debug('productElems[incrementer] == ' + productElems[incrementer].get('href'))
    logging.debug('incrementer == ' + str(incrementer))
