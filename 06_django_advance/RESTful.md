# RESTful

```
GET		https://localhost:8000/articles/1
HTTP method		HOSTNAME	   RESOURCE id
```

1. URI는 자원(명사)만을 표현
2. HTTP method 로 자원을 조작

| HTTP method | URI         | Description       |
| ----------- | ----------- | ----------------- |
| GET         | /articles   | article 목록      |
| GET         | /articles/1 | id=1 article 상세 |
| POST        | /articles   | article 생성      |
| PATCH       | /articles/1 | id=1 article 수정 |
| DELETE      | /articles/1 | id=1 article 삭제 |
| ...         | ...         | ...               |



