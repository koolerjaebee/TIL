import time

start = time.time()

# 답안
N = 1000000

for i in range(2, N+1):  # 2 ~ 10
    is_prime = True
    # x 를 (1 부터 x 까지의 숫자)로 나눠보고,
    # 1 과 x 로만 나누었을 때 나머지가 0이라면
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        pass

end = time.time()
print(end - start)
