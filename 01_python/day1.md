# 190715 python -day1

## Bash

### 단축키

* ctrl + c : 취소
* ctrl + l : 리셋 == clear
* ctrl + backspace : 단어 단위 되돌아가기
* ctrl + d : bash 정리

### 명령어

* 앞 몇 글자를 적은 후 Tab을 누르면 자동완성 해준다.
* / : 가장 근간, home 위에 존재함 == /
* -'option' : 해당 기능의 옵션
* cd : chage directory (그냥 치면 홈으로 감)
  * cd - : 이전 디렉토리
  * cd .. : 부모 디렉토리로 가기
  * cd ~ : 홈 디렉토리 가기
  * cd . : 내 자리 디렉토리로 가기
* mkdir : make directory
  * mkdir -p 'dir'/'dir'/... : 디렉토리 여러개 생성 옵션
* touch : 파일 생성
* rm : 삭제
  * rm a b c d : 여러 파일 삭제 (touch도 가능)
  * rm -r : 디렉토리 삭제
* clear : 리셋 == ctrl + l
* echo : ==print()
* ls : list
  * ls -a : 숨김 포함
* pwd : print working directory
* cp : copy
  * cp 'A' 'B' : A를 복사해서 이름 B로 바꿈
  * cp 'A' 'dir' : A를 디렉토리에 복사
* mv : move
  * mv 'A' 'B' : A를 지금 디렉토리로 옮겨서 B로 바꾸기 == 이름 바꾸기
  * mv 'A' 'dir' : A를 디렉토리로 옮기기

### 강력한 명령어 (위험함)

* sudo : super user do (슈퍼유저 권한을 갖는다)  # 권한이 필요한 것에는 이유가 있다!
* 'command' -f : 강제 실행
* rm -rf 'dir' : 디렉토리와 그 안 모든 컨텐츠 삭제

### git 명령어

* git init : 버전 관리 시작 (.git 생성됨)
* rm -r .git : git 망했을때 다 날려버리는 방법



## Jupyter

print가 아니더라도 Jupyter cell의 마지막 줄은 항상 보여주려고 한다.

In[*] 실행중이라는 뜻

### 단축키

* shift + enter : 다음줄로
* ctrl + enter : 실행
* b : 아래 추가
* a : 위에 추가
* x : 잘라내기
* v : 붙여넣기
* dd : 삭제



## Python

식별자 == 변수

### 오류 메세지

- EOL == end of line

### 컴퓨터의 구조

사람 (cpu)

작업테이블(ram == random access memory)

- 수두루빽빽 모눈종이로 되어 있음



__ : python에서 magical한 기능을 가짐 (매지컬~)

### id()

메모리의 주솟값을 나타낸다

자료의 가장 앞쪽의 주소를 보인다

많이 쓰는 정수들(ex 1, 2 와 같은 작은 정수)은 주소가 정해져있어

어떤 변수도 같은 주소를 가리킨다.

주소값을 바꾼다던지는 할 수 없다 ( 더 low level 언어에서만 가능)



임의의 위치에 데이터값을 넣는 것보다 가리키는 것이 더 빠르다.

데이터 처리 속도 : 추가 vs 제거 == 제거 win because 가리킴을 없앨 뿐 저장 자체는 남아있음

