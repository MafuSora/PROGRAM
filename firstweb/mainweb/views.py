
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


def newpage(request):
    return HttpResponse("new")


def a(request):
    return HttpResponse()


def shop(request):
    return render(request, 'shop.html')


def shop_laptop(request):
    return render(request, 'shop_laptop.html')


def shop_console(request):
    return render(request, 'shop_console.html')


def shop_smartphone(request):
    return render(request, 'shop_smartphone.html')


def first_page(request):
    return render(request, 'firstpage.html')


def second_page(request):
    return render(request, 'secondpage.html')


def mafualbum1_page(request):
    return render(request, "jawaban_Bootstrap.html")
