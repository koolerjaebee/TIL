# n 을 입력받고, 1 부터 n 까지 출력하라
number = 0
while number > 0:
    number = input('n까지 더할 n을 입력하시오 : ')
    number = int(number)

    if number < 1:
        print('1이상의 수를 입력해주세요.')
    else:
        for n in range(number):
            print(n+1)
