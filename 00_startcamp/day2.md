# 190709 startcamp -day2

## What is git?



git: scm(source code manager) / vcs(version control system)

git ==> version 관리를 해주는 감시카메라

ex)

final-처음만들었음.txt



` git init`

`git add '<filename>'` add == 파일 commit 준비 aka "찍습니다"

`git commit -m '<message>'` commit == 상태 저장 aka ''찰칵''

`git commit -m '<message>'`



```bash
$ git remote add origin "URL" # origin은 공유할 일반적인 클라우드 이름 학습중에는 github 사용
$ git remote -v # 연동 상황 확인
$ git push origin master # 사용자 branches

```

### git ignore

.gitignore

`.vscode/`



## Web

```python
import webbrowser
urls=[https://~,
      ~~,
     ] # 브라우저 url

for url in urls:
    webbrowser.open(url)

```

## web 요청과 응답

* 주소 요청(request)과 문서 응답(response)



WYSIWYG(What you see is what you get)

ex) 웹브라우저 문서 (html)



### Scraping

#### kospi

```python
import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
kospi = text.select_one('#KOSPI_now')
print(kospi.text)

```



#### melon top 50

```python
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

```



번외

```python
import requests
import bs4

url = 'https://www.melon.com/chart/'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')
artist = 0
for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artists = row.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    print(rank, title, end=' ')
    for artist in artists:
            print(artist.text, end='')
            print(' ', end='')
    print('')

```



### File Control

### file read

```python
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)

```

### file write

```python
lunches = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')

```



### web + file write

#### melon top50를 파일로 쓰기

```python
import requests
import bs4

url = 'https://www.melon.com/chart/'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')
artist = 0
artists_2 = []
with open('melonTOP50.csv', 'w', encoding='utf-8') as f:
        for row in rows:
                rank = row.select_one('td:nth-child(2) > div > span.rank').text
                title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
                artists = row.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
                for artist in artists:
                        artist = artist.text
                        artists_2.append(artist)                
                f.write(f'{rank}, {title}, {artists_2}\n')
                artists_2=[]

```

