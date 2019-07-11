# 190711 startcamp -day4

## Portfolio

https://startbootstrap.com/themes/ : 포트폴리오 무료 템플릿 사이트(Start Bootstrap)

https://koolerjaebee.github.io/ : github에서 제공해주는 개인 url



## Flask

### html

`placeholder="message here"` : 입력하는 공간에 쓰여있는 글

`autofocus` : 처음 커서 위치를 입력 위치에 둠

`value=""` : 미리 값을 채워놓음



`name` : 서버에서만 주고 받기 위한 지표 `request.args.get()` 로 뽑아 올 수 있다.

`class` : 묶음으로 만들어주는 명령어 `.class`를 통해 모두 선택 가능

`id` : 문서에서 유일한 것 `#id`를 통해 지칭

### python 2 html

```python
from flask import Flask, render_template

@app.route('/dday')
def dday():
    ...
    ...
    return render_template('dday.html', left_days=left.days)  # .days는 일 단위로 변환
```

### python

request와  requests는 다르다

### html 2 python

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Send message</title>
</head>
<body>
    <h1>Send message here</h1>
    <form action="/receive">
        <input type="text" name="msg" placeholder="message here" autofocus>
        <input type="submit" value="보내기">
    </form>
</body>
</html>
```

`float()` : string을 실수화하는 함수



## Chatbot Quest 개론

### telegram

from'재웅' to'친구' contents'밥뭐먹?' ===> 카카오톡 서버 ===> from'친구' to'재웅' contents'ㄴ'

### Chatbot

from'재웅' to'Bot' contents'로또' ===> telegram server  =(포워딩)==> BOT ===> Flask (연산)***(신경쓸 곳)

from'Bot' to'재웅' contents'6개 수'<===                           <==========         <===



## 암호화

method의 종류

* GET

* POST

GET : 내놔 (받는 과정)

POST : 가져라 (보내는 과정, 중요한 것을 보낼 때 사용)





