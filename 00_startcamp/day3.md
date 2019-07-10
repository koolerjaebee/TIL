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

