
# 1
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
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


def mafualbum2_page(request):
    return render(request, "Album2.html")


# def shop_laptop_list(request):
#     try:

#         category_laptop = Category.objects.get(pk=1)
#         #pk == primary_key
#         if(request.GET == {}):
#             product_laptop = Product.objects.filter(category=category_laptop)
#         else:
#             form = SearchForm(request.GET)
#             print(form.is_valid())
#             if (form.is_valid()):
#                 product_laptop = Product.objects.filter(category=category_laptop).filter(
#                 name__contains=request.GET['product_name'])

#             else:
#                 return render(request, 'shop_laptop_list.html', {'available': False})

#         # WHERE name like 'chrome'
#         if(product_laptop.count() != 0):
#             return render(request, 'shop_laptop_list.html', {'product_list': product_laptop, 'available': True})
#         else:
#             return render(request, 'shop_laptop_list.html', {'available': False})
#     except:
#         return HttpResponse("Terjadi Error")

def shop_laptop_list(request):
    try:
        print(request.GET)
        category_laptop = Category.objects.get(pk=1)

        if(request.GET == {}):
            product_laptop = Product.objects.filter(category=category_laptop)
        else:
            form = SearchForm(request.GET)
            print(form)
            print(form.is_valid())

            # if(form.is_valid()):
            if request.GET ["price_min"] != "" and request.GET["price_max"] != "" :
                product_laptop = Product.objects.filter(category=category_laptop).filter(
                    price__gt=int(request.GET['price_min'])).filter(price__lt=int(request.GET['price_max']))
                print(product_laptop)
            else:
                return render(request, 'shop_laptop_list.html', {'available': False})

        if(product_laptop.count() != 0):
            return render(request, 'shop_laptop_list.html', {'product_list': product_laptop, 'available': True})
        else:
            return render(request, 'shop_laptop_list.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")
