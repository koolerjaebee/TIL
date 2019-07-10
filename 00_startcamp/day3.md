# 190708 startcamp -day3

## Terminal

`input()` : 입력 값을 받는다

$ : 프롬프트 aka 'I'm ready to hear'

ctrl + c : 입력 대기상태 취소

ctrl+ d : 터미널 종료

작업 단위 하나 하나는 '프로세스' 라고 부른다.

## Python

\ + ' : 문자열에 '을 넣는법

`type()` : 무슨 클래스의 변수인지 확인 ex) string, int ...

`list()` : 리스트화 함수 ex) `word == 'world'; list(word) == ['w', 'o', 'r', 'l', 'd'] `

### 딜레마

`print(random.sample(list(range(1,46)),6))` ==> 한 줄로 코드 작성 가능

but 가독성이 바닥이 됨

### string 변수 넣기

```python
import random

meal = random.choice(['아침', '점심', '저녁'])
string = '나는 {} 을 먹는다'.format(meal)

#OR

string f'나는 {i+1} 을 먹는다'.
```



## Web 서버 체험

```python
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/hi')
def hi():
    return 'hi'


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


if __name__ == '__main__':
    app.run(debug=True)

```



flask : 서버 구성 import

hard coding : 정확한 입력을 필요로 함

variable routing : 좀 더 유연한 방식

`number ** 3` : 제곱 연산



## html 작성 방식

`<DOCTYPE html>` : html 선언

H : Hyper

T : Text

M : Markup

L : Language



```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
    </head>
    <body>
        <h1>Today I Learned</h1>
        <h2>Learn Flask</h2>
        <ol>
            <li>pip install Flask</li>
            <li>touch app.py</li>
            <li>python app.py</li>
        </ol>
        <h2>Learn HTML</h2>
        <ul>
            <li>doctype html</li>
            <li>head, body</li>
            <li>h1, h2, ol, ul, li</li>
        </ul>
    </body>
</html>

```



## Data Mining Method

1. Scrapping
2. API
3. Package