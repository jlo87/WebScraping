# Python code that can parse HTML with the Beautiful Soup Module.
# In this example, I want to find the price of a particular book from bookoutlet.com.

import bs4, requests

def getBookOutletPrice(productUrl): 
	res = requests.get(productUrl) # Request to download the page
	res.raise_for_status() # Raise an Exception if there is an issue

	soup = bs4.BeautifulSoup(res.text, 'html.parser') # Passed html.parser to dismiss the warning.
	elems = soup.select('#color-panel > div > div:nth-child(2) > div.col-md-8 > table > tbody > tr:nth-child(5) > td:nth-child(2) > strong > span')
	return elems[0].text





price = getBookOutletPrice('https://bookoutlet.com/Store/Details/9781593278786B')
print('The price is ' + price)
