# 190731 WEB -day3

## html

### block (ex <div></div>)

#### 속성

- div
- h1 ~ h6 / p
- ol, ul, li / hr
- table / form

#### 특징

- 가로 끝까지 차지한다
- content - padding - margin 으로 이루어져있음

- 내용물이 없으면 안잡힌다

- 항상 새로운 line 에서 시작
- 기본으로 width 100%
- width height margin padding 속성 지정 가능
- block 요소 안에 inline 요소들 포함 가능



### inline

#### 속성

- span
- a
- strong, em, del
- img
- br
- input, select
- textarea
- button

#### 특징

- 새로운 라인에서 시작하지 않으며 문장 중간에 쓸 수 있다
- content 너비만큼 가로폭을 차지한다
- width height margin padding 속성 지정 불가능 따라서 행간으로 지정
- inline 요소 뒤에 공백(/n, space)이 있으면 자동으로 space(4px)가 들어간다
- inline 요소 안에 block 요소 포함 불가능



### inline block

#### 특징

- inline의 한줄표시 + block의 margin, padding, width, height
- content 너비만큼 가로폭
- display: inline-block 인 요소들 뒤에 공백은 space * 4
- 상하 여백: margin과 line height 로 가능



### static box

#### 특징

- position 의 default
- 위 => 아래, 왼 => 오
- 부모요소 <=> 자식요소 부모의 위치가 기준점
- 좌푯값을 줘도 안됨