my = [1, 2, 3, 4, 5, 6]
real = [1, 2, 3, 4, 5, 7]
# bonus = 6
bonus = [6]  # 내 정답 bonus

# 내 정답

differences_main = list(set(real)-set(my))
differences_sub = list(set(bonus)-set(my))
match_count_main = len(differences_main)
match_count_sub = len(differences_sub)

if match_count_main == 0:
    result = '1등'
elif match_count_main == 1 and match_count_sub == 0:
    result = '2등'
elif match_count_main == 1 and match_count_sub == 1:
    result = '3등'
elif match_count_main == 2:
    result = '4등'
elif match_count_main == 3:
    result = '5등'
else:
    result = '꽝'

print(result)

# 로또 코딩
# my 와 real의 숫자가 모두 같으면 1등
# my 와 real 이 5개가 같고 나머지가 하나가 bonus 면 2등
# 5개 3등, 4개 4등, 3개 5등, 나머지 꽝

# 첫 번째 정답 == 가장 파이썬스럽지 않은 코드

# match_count = 0
# is_bonus = False

# for i in my:

#     if i == bonus:
#         is_bonus = True

#     for j in real:
#         if i == j:
#             match_count +=1

# if match_count == 6:
#     result = '1등'
# elif match_count == 5:
#     if is_bonus:
#         result = '2등'
#     else:
#         result = '3등'
# elif match_count == 4:
#     result = '4등'
# elif match_count == 3:
#     result = '5등'
# else:
#     result = '꽝ㅠ'

# print(result)

# 두번째 정답

# match_count = 0

# for i in my:
#     for j in real:
#         if i == j:
#             # match_count = match_count + 1
#             match_count += 1

# if match_count == 6:
#     result = '1등'
# elif match_count == 5:
#     if bonus in my:
#         result = '2등'
#     else:
#         result = '3등'
# elif match_count == 4:
#     result = '4등'
# elif match_count == 3:
#     result = '5등'
# else:
#     result = '꽝ㅠ'

# print(result)

# 세번째 정답

# match = set(my).intersection(set(real))
# match_count = len(match)
# ​
# if match_count == 6:
#   result = '1등'
# elif match_count == 5:
#   if bonus in my:
#     result = '2등'
#   else:
#     result = '3등'
# elif match_count == 4:
#   result = '4등'
# elif match_count == 3:
#   result = '5등'
# else:
#   result = '꽝ㅠ'
# ​
# print(result)
