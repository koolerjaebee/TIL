from django.shortcuts import render, HttpResponse
from art import *


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['1943', '3-d', '3d_diagonal', 'alpha', 'random']
    context = {'fonts': fonts}
    return render(request, 'utils/art.html', context)


def output(request):
    user_word = request.GET.get('user-word')
    user_font = request.GET.get('user-font')

    result = text2art(user_word, font=user_font)
    context = {'result': result}

    return render(request, 'utils/output.html', context)


def throw(request):
    lol_chess_items = {
        'B.F. 대검': 'a', '곡궁': 'b', '쇠사슬 조끼': 'c', '음전자 망토': 'd',
        '쓸데없이 큰 지팡이': 'e', '여신의 눈물': 'f', '거인의 허리띠': 'g', '뒤집개': 'h'
    }
    context = {'items': lol_chess_items}
    return render(request, 'utils/throw.html', context)


def catch(request):
    lol_chess_combined_items = {
        'aa': '무한의 대검', 'ab': '신성의 검', 'ac': '수호 천사', 'ad': '피바라기',
        'ae': '마법공학 총검', 'af': '쇼진의 창', 'ag': '지크의 전령', 'ah': '요우무의 유령검',
        'bb': '고속 연사포', 'bc': '유령 무희', 'bd': '저주받은 칼날', 'be': '구인수의 격노검',
        'bf': '스태틱의 단검', 'bg': '거대한 히드라', 'bh': '몰락한 왕의 검', 'cc': '가시 갑옷',
        'cd': '파쇄검', 'ce': '강철의 솔라리 펜던트', 'cf': '얼어붙은 심장', 'cg': '붉은 덩굴정령',
        'ch': '기사의 맹세', 'dd': '용의 발톱', 'de': '이온 충격기', 'df': '침묵',
        'dg': '서풍', 'dh': '루난의 허리케인', 'ee': '라바돈의 죽음모자', 'ef': '루덴의 메아리',
        'eg': ' 모렐로노미콘', 'eh': '유미', 'ff': '대천사의 포옹', 'fg': '구원',
        'fh': '다르킨', 'gg': '워모그의 갑옷', 'gh': '얼어붙은 망치', 'hh': '대자연의 힘'
    }

    item_1 = request.GET.get('item-1')
    item_2 = request.GET.get('item-2')
    item_result = ''.join(sorted(item_1 + item_2))
    result = lol_chess_combined_items.get(item_result)
    context = {'result': result}
    return render(request, 'utils/catch.html', context)
