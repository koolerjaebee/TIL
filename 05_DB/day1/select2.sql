-- SQLite
-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age = 30;
-- SELECT * FROM users WHERE age >= 30;

-- SELECT first_name FROM users WHERE age >= 30;

-- users 에서 age 30이상 성이 '김' 인 사람의 성과 나이만 가져온다면?
-- SELECT age, last_name FROM users  -- users 에서 사람의 성과 나이만 가져온다
-- WHERE age >= 30 AND last_name = '김'  -- age 30이상 이상인 '김'
-- LIMIT 10;  -- 10개만

-- COUNT
-- SELECT COUNT(*) FROM users;

-- AVG, SUM, MIN, MAX (숫자 컬럼만 가능)
-- 30살 이상인 사람의 평균나이
-- SELECT AVG(age) FROM users
-- WHERE age >= 30;

-- users 에서 잔액이 가장 높은 사람과 잔액
-- SELECT first_name, MAX(balance) FROM users

-- users 에서 30살 이상인 사람의 계좌 평균 잔액은?
-- SELECT AVG(balance) FROM users
-- WHERE age >= 30;

-- wild cards
-- SELECT * FROM users WHERE age LIKE '2_';

-- users 에서 지역번호가 02 인 사람만
-- SELECT * FROM users WHERE phone LIKE '02-%'

-- users 에서 이름이 '준' 으로 끝나는 사람
-- SELECT * FROM users WHERE first_name LIKE '%준'

-- users 에서 전화번호 중간에 5115가 들어가는 사람
-- SELECT * FROM users WHERE phone LIKE '%5114%'

-- users 에서 나이순으로 오름차순 정렬하여 상위 10개
-- SELECT * FROM users
-- ORDER BY age ASC LIMIT 10;

-- SELECT * FROM users
-- ORDER BY age DESC LIMIT 10;

-- 우선순위 2개(age, balance)를 설정
-- SELECT * FROM users
-- ORDER BY age, balance LIMIT 10;

--users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 뽑아보면?
SELECT last_name, first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;