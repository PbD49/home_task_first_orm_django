from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    '''Перенаправляет на страницу католог телефонов'''
    return redirect('catalog')


def show_catalog(request):
    '''Обработчик запроса для отображения каталога телефонов в веб-приложении'''
    context = {}
    if request.GET:
        if request.GET['sort'] == 'name':
            lst_obj = sorted(Phone.objects.all(), key=lambda x: x.name)
            context.setdefault('phones', lst_obj)
        elif request.GET['sort'] == 'min_price':
            lst_obj = sorted(Phone.objects.all(), key=lambda x: x.price)
            context.setdefault('phones', lst_obj)
        elif request.GET['sort'] == 'max_price':
            lst_obj = sorted(Phone.objects.all(), key=lambda x: x.price, reverse=True)
            context.setdefault('phones', lst_obj)
    else:
        context = {'phones': Phone.objects.all()}
    template = 'catalog.html'
    return render(request, template, context)


def show_product(request, slug):
    '''Обработчик для отображения страницы с деталями продукта'''
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug)[0]}
    return render(request, template, context)
