import requests
from bs4 import BeautifulSoup
import urllib2


url = 'https://crx.dam.io/pages/{}.html'.format(pagenumber)
r = requests.get(url)
soup = BeautifulSoup(r.text)
smallwithext = [small.find('a').contents for small in soup.findAll('small', {"class": "extlink"})]
for a in smallwithext:
	print str(a[0])[1:]