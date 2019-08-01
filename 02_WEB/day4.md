# 190801 WEB -day4

## python 과목 테스트

### 1. built-in function 아닌 것은?

`sqrt()`



### 2. 시퀀스자료의 특징이 아닌 것은?

기본적으로 정렬이 되어 있지만, 사용자 임의대로 순서를 변경할 수 있다.



### 3. names = ['John', 'Ron', 'James', 'Betty']

`print(names[-2][-2]) == 'e'`



### 4. p3.population?

3



### 5. 오류가 나는것은?

#### my complex = 3+4j

#### my_list= [1, 2, 3]

#### my_dict = {1: 1, 2: 2}

my_complex.real()



### 7. print 되는 class는?

dict (dictionary가 아니다)



### 8. 함수에 대한 설명으로 옳지 않은 것을 고르시오.

함수에서 return을 작성하지 않으면 코드 실행시 오류가 실행된다.



### 9. 다섯개의 정수 0을 가진 리스트를 만드는 방법 중 틀린 것을 고르시오.

numbers=[]; numbers.append(0*5)



### 10. result = 4 + True + False + 5

10 (자동으로 형변환이 된다)



### 12. d1 = {'d': dict()}, d2 = dict(d={}) 

d1 == d2 == {'d': {}}

d1의 value와 d2의 value는 모두 비어있는 딕셔너리다.



###  13.

'hong' 



### 14.

```python
my_int = 3

isinstance(int, my_int)
my_int == 3
isinstance(my_int, 3)
type(my_int) == int  # 정답
```



### 15.

`p3 = Person(age=3, name='kang')`

순서 바껴도 키워드를 선언해주면 된다.



### 16.

```python
word = 'python'

indexing = word[3:8]
print(indexing)
# 정답 hon
```



### 17.

return 없으니 None



### 18.(여기부터 난이도 상)

enumerate(string) : list로



### 19.

.update() : 값 자체는 None을 반환한다.

보기 중에는 답이 없다.



## Bootstrap

### 많이 쓰는 Components

- Button
- Card
- Carousel(회전목마)
- Dropdowns
- Forms
- Jumbotron
- List group
- Navs

### bootstrap 구조

container > row (12개의 grid)

col- (xs) sm  md ...

col-3 (3/12)

