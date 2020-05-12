from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'menu/home.html', {})


def menu(request):
    menuItems = models.Menu.objects.all().values()
    menuList = []
    count = 0
    innerList = []
    for items in menuItems:
        count += 1
        print(items)
        items['item_img'] = items['item_img'].split('menu/')[1]
        innerList.append(items)
        if count/4 == 1 and count != 0:
            menuList.append(innerList)
            innerList = []

    return render(request, 'menu/menu.html', {'menuitems': menuList})