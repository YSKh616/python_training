import requests
import bs4

url = "https://cookpad.com/"
html = requests.get(url)
soup = bs4.BeautifulSoup(html.parser)
title_tag = soup.title

# print(title_tag)


