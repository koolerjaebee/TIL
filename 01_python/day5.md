# 190722 python -day5

## 공식표현

`<class str>.replace(old, new[, count])`

.strip([chars])

- <class str> : str 형 자료를 넣으라는 뜻
- [, count] : 필요할 때 추가하는 부분
- [chars] : 문자형으로 넣으라는 뜻
- update(*others) : 여러개가 가능하다는 뜻



## Data structure

- call by value : 값으로 부르다 (그 자체에 값을 저장) ex) str, number, bool

- call by reference : 참조로 부르다 (주소값을 가리킨다) ex) list, tuple, set, dictionary
  - 특히 mutable(바꿀수 있는)이 문제가 생길 수 있다.



## 메소드의 return 여부 (원본 변화 여부)

### list

- 조회하는 것 : d원본 == 0, return != 0
- 그 외 : d원본 != 0, return == None

### string

- 모든 함수 : d원본 == 0, return != 0



### 결론

- mutable(대괄호[] & 중괄호{}) : (거의 대부분) 원본이 바뀜
- immutable(그외) : 원본이 '못' 바뀜



## List Comprehension

`cubic_list = [number ** 3 for number in numbers]`

`even_list = [number for number in numbers if number % 2 == 0]`



순서 : for / in / if



## The Zen of Python

```python
import this
​```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
​```

```

== '답은 정해져 있다!'

## 자주 쓰는 메소드

### 문자열

- .join()
- .replace()

- .strip()
- .find()
- .split()

### 리스트

- .append()
- .remove()
- .count()
- .sort()
- 복사
- List comprehension ( [`elem for elem_list in list if True`] )

### 딕셔너리

- .get()

### 세트

- remove() vs discard() 만 기억하자



## 팁

`n % 2` 이 자체가 홀수 판별식 (나머지가 나오면 True 없으면 False가 나오기 때문)

값이 0 또는 1 나오는 식을 잘 보면 코드를 더 짧게 쓸 수 있다.