import requests, bs4, os

url = 'http://xkcd.com/'
os.makedirs('xkcd', exist_ok = True)

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    r = requests.get(url)
    r.raise_for_status()

    r_soup = bs4.BeautifulSoup(r.text)

    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicURL = 'http:' + comicElem[0].get('src')
