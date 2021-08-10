
# 1
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def landing_page(request):
    return HttpResponse("Hello,World")


def second_page(request):
    return HttpResponse('secondpage')


def count(request, angka):
    angka += 1
    return HttpResponse(str(angka))


def sapa(request, nama):

    return HttpResponse("halo"+nama)


def htmlcoba(request):
    return render(request, "examples.html")


def funcbaru(request):
    return HttpResponse("papa")


def mainpage(request):
    return render(request, index.html)
