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
        if count % 4 == 0 and count != 0:
            menuList.append(innerList)
            innerList = []
    response = render(request, 'menu/menu.html', {'menuitems': menuList, 'user': request.user})
    return response


def cart(request):
    menuItems = models.Menu.objects.all().values()
    print(request.COOKIES)
    order, total = retrieve_items(menuItems, request)
    print(order, total)
    response = render(request, 'menu/cart.html', {'user': request.user, 'order': order, 'total': total})
    return response


def retrieve_items(items, request):
    order = []
    total = 0
    for i in items:
        item = {}
        # print(request.COOKIES[str(i['item_id'])])
        if request.COOKIES.get(str(i['item_id'])) != str(0) and request.COOKIES.get(str(i['item_id'])) is not None:
            updated_price = (float(i['item_price'].split('$')[1]))*int(request.COOKIES.get(str(i['item_id'])))
            item.update({'name': i['item_name'], 'quantity': request.COOKIES.get(str(i['item_id'])), 'price': updated_price})
            if '$' in i['item_price']:
                item.update({'symbol':'$'})
                total += updated_price
            order.append(item)
    return order, str(total)
