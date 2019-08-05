# 190805 server intro -day1

## Django

### M(Model) T(Templates) V(Views)

```bash
$ pip install django
$ django-admin startproject first_project
```

all capital 변경 금지

project 시작시 manage.py가 있는 곳이 기준



views는 중간관리자



### django의 request / response 과정

| Client                   |                    | master URL |            | app URL                 |
| ------------------------ | ------------------ | ---------- | ---------- | ----------------------- |
| https://DOMAIN/pages/... | ===><br />Request  | pages/     | ===><br /> | pages/help              |
| help.html                | <===<br />Response | ===<br />  | ===<br />  | views.py<br />templates |

