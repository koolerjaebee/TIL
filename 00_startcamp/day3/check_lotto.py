# my = [1, 2, 3, 4, 5, 6]
# real = [1, 2, 3, 4, 5, 7]
# bonus = 6

# 로또 코딩
# my 와 real의 숫자가 모두 같으면 1등
# my 와 real 이 5개가 같고 나머지가 하나가 bonus 면 2등
# 5개 3등, 4개 4등, 3개 5등, 나머지 꽝
import random

my_numbers = map(int, input('로또번호 6개를 입력해주세요 : ').split())
my_numbers = list(my_numbers)
for my_number in my_numbers:
    if my_numbers[my_number] > 45 or my_numbers[my_number] < 1:
        print('1과 45 사이의 값을 넣어주세요')
    else:
        my_numbers = my_numbers[:6]
        my_numbers = sort(my_numbers)
        lotto_numbers = list(range(1, 46))
        lotto_numbers = sort(lotto_numbers)
        if
