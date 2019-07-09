import requests
import bs4
# kospi 프로그래밍

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
kospi = text.select_one('#KOSPI_now')
print(kospi.text)
