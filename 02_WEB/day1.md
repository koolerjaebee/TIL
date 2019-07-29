# 190729 WEB -day1

## git

git이 관리하는 폴더 ==> repository

git이 관리 안하는 폴더 ==> directory

git 꼬이면 : rm -r .git/



shift + insert : 복사 붙여넣기

### git 시작

```bash
$ touch .gitignore
$ git init
```

### git status

```bash
$ git status
On branch master

No commits yet

Untracked files:
	(use "git add <file>..." to include in what will be committed)
	
		.gitignore
		
nothing added to commit but untracked files present (use "git add" to track)
```

### git add / rm

```bash
$ git add .gitignore
$ git status
On branch master

No commits yet

Changes to be committed:
	(use "git rm --cached <file>..." to unstage)
	
		new file:	.gitignore
		

$ git rm --cached .gitignore
rm '.gitignore'
$ git status
On branch master

No commits yet

Untracked files:
	(use "git add <file>..." to include in what will be committed)
	
		.gitignore
		
nothing added to commit but untracked files present (use "git add" to track)
```

### modified

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
	(use "git rm --cached <file>..." to unstage)
	
		new file:	.gitignore
		
Changes no staged for commit:
	(use "git add <file>..." to update what will be committed)
	(use "git checkout -- <file>..." to discard changes in working directory)
	
		modified:	.gitignore
```

### git diff

```bash
$ git diff
diff --git aendgame.txt b/endgame.txt
index e59de29..8636389 100644
--- a/endgame.txt
+++ b/endgame.txt
@@ -0,0 +1,26 @@
+시험
+험담
...

```

### :

- 너무 길어지면 생김
- u : 위로
- d : 아래로
- q : 나가기

### 올리면 안되는 것을 올렸을 때

git add 까지는 괜찮음

git rm --cached 를 통해 잘못 올린 것 삭제 가능

그리고 .gitignore에 추가

*** .gitignore의 중요성

commit까지는 그래도 괜찮지만

push부터는 답 없어지기 시작하다가

push 후 commit 까지하면 답 x

### directory

디렉토리만 생긴 것은 git status에 나오지 않음

디렉토리 않에 파일이 생기면 그때 디렉토리를 트랙킹

하지만 그 속 컨텐츠는 안봄

### 디렉토리 지우는 법

- rm -r <directory>/

### commit / add

commmit은 위치 상관 x

add는 물론 위치 상관 o

내 위치를 항상 주의하자



code . : 디렉토리 위치에서 VS code 실행



### git remote

git remote add <name> <URL> (<name>은 버전관리중인 프로젝트의 이름)

git remote -v

git remote rm <name>

git push <name> master (&& git push <name> master)

### 협업

git clone <URL> <dir> (dir은 선택, 안쓰면 원래 이름으로 생성)

download : .git 안가지고 옴

clone : .git 가지고 옴

Head : 나

두개의 commit이 겹칠때는 변경사항을 봐서 고를 수 있다.(VS code 클릭 지원)

## vim (vi)

```bash
$ vi <filename>
```

#### edit mode

- 편집만 됨
- esc : command mode 들어가기

#### command mode

- dd : 한줄 삭제
- u : 되돌리기
- i : (끼워넣기) edit mode 들어가기

- ':' : 명령어 입력 시작
- :w : 저장
- :q : 나가기

- :q! : 강제로 나가기
- :wq : 저장하고 나가기



## Intro to WEB Service

Client(고객) <====> Server(해주는 사람)

=>request				response<=



요청(Request)의 종류

- Get(받다)
- Post(보내다)

#### 결론

우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.



- Static web : 클라이언트가 요청을 보내면 응답을 한다.

HTTP(S)(Hyper Text Transfer Protocol Secure)



Hyper Text Markup Language (역할표시언어) == HTML

### 웹 표준

- W3C
- ?



### html 요소

- head
- body



### 한가지만 기억하자!

# 큰제목(이 문서에서 가장 큰 제목!)

## 작은제목. 1

본문본문

- 리스트1
- 리스트2
- 리스트3

## 작은제목. 2

본문본문

# 큰 제목(2개 존재할 수 없다)

### 좀더 작은제목

#### 좀더더 작은 제목

h1은 하나만 존재해야한다.

h2는 두번째로 큰 글이 아닌 구조화에서 두번째로 중요한 내용이다라고 생각해야된다.