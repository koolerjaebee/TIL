import time

start = time.time()

# GO!
N = 1000000
N_check = int(int(N)**0.5)

# print('2')
for number in range(3, N+1):
    number_check = int(number**0.5)
    for div in range(2, number_check+1):
        if number % div == 0:
            break
    else:
        pass

end = time.time()
print(end - start)
