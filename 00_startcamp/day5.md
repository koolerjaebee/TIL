# 190712 startcamp -day5

## Python

### set(집합)

* [1, 2, 3] => list

* {1, 2, 3} => set

* (1, 2, 3) => tuple

* {'a' : 'A'} => dict

`set()` : 집합으로 만드는 함수

`len()` : 요소 갯수 확인 함수

`list in b`  : list 안에 b가 있느냐 True False 값을 가짐

## Chatbot Quest

### New project

```bash
$ touch .gitignore # venv/; .vscode/
$ git init
$ py -m venv venv
$ #F1 Python: Select interpreter
$ touch app.py
$ mkdir templates
$ cd templates
$ touch send.html
$ touch write.html
$ cd ..
$ git add .
$ git commit -m 'first commit'

```



### Local host

http://127.0.0.1:5000/ ==> 내 컴퓨터 내에서만 요청 가능

ngrok : 외부에서 들어오게 해주기 위해서 사용

:5000 ==> 포트 번호(디폴트)

:80 ==> url에 표시되지 않는 포트 번호

python anywhere ==> cloud computing server ex)AWS

Postman ==> 여러 기능이 있는 브라우저, 특히 주고받는 데이터를 수정하는 것에

### ngrok

![1562921432067](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562921432067.png)



https://api.telegram.org/bot811882579:AAE402Yov2M9Cl9vhJtcdvIpWWEgFjkqd84/setWebhook?url=https://67843303.ngrok.io/2d3a6738ca3d8cd2da75686679806791d41c9582

![1562921379893](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562921379893.png)