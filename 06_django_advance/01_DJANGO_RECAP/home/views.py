from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'home/index.html')


def guess(request):
    return render(request, 'home/guess.html')


def answer(request):  # 채점 구간
    count = 0
    if request.POST.get('q1') == '93.4.13':
        count += 1
    if request.POST.get('q2') == '250':
        count += 1
    if request.POST.get('q3') == 'Galaxy S10+':
        count += 1
    context = {'count': count}
    return render(request, 'home/answer.html', context=context)
