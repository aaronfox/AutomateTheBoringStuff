#! python3
#
# amazonReviews.py - opens the link to reviews for a single product

import requests, sys, webbrowser, bs4, pyperclip

headerInfo = {"User-Agent": "Mozilla/5.0"}

product = ''

if len(sys.argv) > 1:
    # use command line arguments
    product = ' '.join(sys.argv[1:])
else:
    # use whatever user has copied to clipboard
    product = pyperclip.paste() 


# first, search for product on amazon
res = requests.get('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + product, headers = headerInfo)
res.raise_for_status()

# search for product page
productSoup = bs4.BeautifulSoup(res.text, 'html.parser')
productElems = productSoup.select('.a-link-normal.s-access-detail-page.a-text-normal')

incrementer = 0
# skip over the sponsored links and go to the product the user wants
while productElems[incrementer].get('href')[:3] != 'htt':
    incrementer += 1
productPage = productElems[incrementer].get('href')


# obtain the product page, which contains the link to the reviews
productPageRes = requests.get(productPage, headers = headerInfo)
productPageRes.raise_for_status()

# find the link to the reviews
productPageSoup = bs4.BeautifulSoup(productPageRes.text, 'html.parser')
productPageElems = productPageSoup.select('.a-link-emphasis.a-nowrap')

reviewPage = productPageElems[0].get('href')
if reviewPage[:3] != 'htt':
    reviewPage = 'http://amazon.com/' + reviewPage

# open the link to the reviews
webbrowser.open(reviewPage)
