# fizz buzz => 3의 배수에서 fizz/ 5의 배수 buzz / 15의 배수 fizzbuzz

end_number = int(input('fizzbuzz 놀이를 수행할 마지막 수를 입력하세요 : '))
for n in range(end_number):
    if (n+1) % 15 == 0:
        print('fizzbuzz', end=' ')
    elif (n+1) % 3:
        print('fizz', end=' ')
    elif (n+1) % 5 == 0:
        print('buzz', end=' ')
    else:
        print(n+1, end=' ')
