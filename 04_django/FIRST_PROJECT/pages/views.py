from django.shortcuts import render, HttpResponse
import json

# Create your views here.


def index(request):
    return HttpResponse('Hi django! :)')


def about(request):
    me = {
        'name': '허재웅',
        'role': 'Student',
        'email': 'koolerjaebee@gmail.com'
    }

    return HttpResponse(json.dumps(me))


# HTML 을 내보내고 싶다.
def portfolio(request):
    return render(request, 'portfolio.html')


def help(request):
    return render(request, 'help.html')
