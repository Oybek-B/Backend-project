from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world')



def index(request):
    return render(request, 'store/index.html')
