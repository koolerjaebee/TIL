import time

start = time.time()

number = 1000000
prime_list = [2]

for i in range(3, number):
    for prime in prime_list:
        if prime > (number ** 0.5):
            break
        if i % prime == 0:
            break
    else:
        prime_list.append(i)

pass

end = time.time()
print(end - start)
