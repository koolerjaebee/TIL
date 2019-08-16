# 190812 algorithm -day1

### 시간 복잡도(Time Complexity)

- O(n) : 최악의 경우
- Ω(n) : 최선의 경우
- θ(n) : 평균



리스트 append 보다 처음부터 리스트의 크기를 크게 하는 것이 속도를 향상시킨다.

str 함수가 일반적으로 속도가 빠르다.



### 언어의 방식

#### Compiler 방식 

- compile 과정(object) o & link 과정 o (C C++ Java)
- 운영체제가 실행시킴

#### Interpreter 방식

-  compile 과정 x 바로 실행 가능 (basic python)
- Interpreter가 실행시킴
- 속도가 느림



### 알고리즘 기법

#### 완전 검색(Exhaustive Search)

모든 경우의 수를 나열해보는 기법

Brute-force 혹은 generate-and-test 기법이라고도 불리 운다.

일단 완전검색으로 시작하라 (해답을 찾아내지 못할 확률이 작기 때문)

#### 탐욕(Greedy) 알고리즘

최적해를 구하는 데 사용되는 근시안적인 방법

순간 최적 경로 설정



### 정렬

- 버블 정렬 (Bubble Sort)
- 카운팅 정렬 (Counting Sort)
- 선택 정렬 (Selection Sort)
- 퀵 정렬 (Quick Sort)
- 삽입 정렬 (Insertion Sort)
- 병합 정렬 (Merge Sort)



#### 버블 정렬

인정하는 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

시간 복잡도 : O(n^2)



#### 카운팅 정렬

항목들의 순서를 결정하기 위해 집하베 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

시간 복잡도 : O(n + k) (n은 리스트 길이, k는 정수의 최댓값)