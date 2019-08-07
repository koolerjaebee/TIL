from django.shortcuts import render
import requests
import bs4
from real_data.models import HotIssue


def start(request):
    return render(request, 'real_data/start.html')


def end(request):
    url = 'https://datalab.naver.com/keyword/realtimeList.naver/'
    headers = {'user-agent': ':('}
    response = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(response, 'html.parser')

    for num in range(1, 21):
        date = soup.select_one('#content > div > div.section_serch_area > div > div.date_indo > a.date_box._date_trigger > span.date_txt._title_ymd').text
        time = soup.select_one('#content > div > div.section_serch_area > div > div.time_indo > a.time_box._time_trigger > span.time_txt._title_hms').text
        rank = int(soup.select_one(f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({num}) > a > em').text)
        keyword = soup.select_one(f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({num}) > a > span').text
        hot_issue = HotIssue.objects.create(date=date, time=time, rank=rank, keyword=keyword)

    return render(request, 'real_data/end.html')
