# 190708 startcamp -day1

## 컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터란, 계산기다.

### 프로그래밍

명령어의 집합. 쉽게 일 시키는 것

### 언어

말, 약속



## Python 기초 문법 3형식

1. 저장
2. 조건
3. 반복



## Python 함수

파이썬 함수에는 내장 함수와 외장 함수가 있다.

* 내장 함수
  * `print()` : 출력하는 함수
  * `range()` : 리스트를 생성하는 함수
  * `list()` : 범위(range)를 생성하는 함수

* 외장 함수
  * `random` : 랜덤 관련 함수들의 묶음
  * `random.choice()` : 리스트에서 1개 무작위 선택
  * `random.sample(p, n)` : 모집단에서 n 개의 요소를 무작위 비복원 선택

### 미세먼지 확인하기

```python
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&ServiceKey={}&ver=1.3&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text
dust = int(gn.pm10Value.text)

#print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))
if dust < 30:
    print('{0} 기준: 서울시 {1}의 미세먼지 농도는 매우좋음 입니다.'.format(time, location, dust))
elif dust<50:
    print('{0} 기준: 서울시 {1}의 미세먼지 농도는 좋음 입니다.'.format(time, location, dust))
elif dust<80:
    print('{0} 기준: 서울시 {1}의 미세먼지 농도는 보통 입니다.'.format(time, location, dust))
elif dust<150:
    print('{0} 기준: 서울시 {1}의 미세먼지 농도는 나쁨 입니다.'.format(time, location, dust))
else:
    print('{0} 기준: 서울시 {1}의 미세먼지 농도는 매우나쁨 입니다.'.format(time, location, dust))
```



### 로또 번호 추첨 하기

```python
import random
numbers=list(range(1, 46))
lucky_numbers=random.sample(numbers,6)
lucky_numbers.sort() # 리스트 오름차순
print(lucky_numbers)
```



| name              | age     |
| ----------------- | ------- |
| \|(shift+\)name\| | \|age\| |


$$
수식 : $$
$$


