import requests
import bs4

url = 'https://www.melon.com/chart/'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)
