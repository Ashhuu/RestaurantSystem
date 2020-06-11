from django.shortcuts import render
from . import models


def index(request):
    menuItems = models.Menu.objects.all()[:4]
    menuList, innerList = getMenuItems(menuItems)
    specialItems = models.Menu.objects.filter(special=True)
    if len(specialItems) < 1:
        specialItems = None
    return render(request, 'menu/home.html', {'menuitems': menuList, 'innerList': innerList,
                                              'specialItems': specialItems})


def menu(request):
    menuItems = models.Menu.objects.all()
    menuList, innerList = getMenuItems(menuItems)
    response = render(request, 'menu/menu.html', {'menuitems': menuList, 'user': request.user, 'innerList': innerList})
    return response


def getMenuItems(menuItems):
    menuList = []
    count = 0
    innerList = []
    for items in menuItems:
        count += 1
        print(items)
        innerList.append(items)
        if count % 2 == 0 and count != 0:
            menuList.append(innerList)
            innerList = []
    if len(innerList) > 0:
        pass
    else:
        innerList = None
    return menuList, innerList


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
            updated_price = (float(i['item_price'].split('Rs.')[1])) * int(request.COOKIES.get(str(i['item_id'])))
            item.update(
                {'name': i['item_name'], 'quantity': request.COOKIES.get(str(i['item_id'])), 'price': updated_price})
            if '$' in i['item_price']:
                item.update({'symbol': '$'})
                total += updated_price
            elif 'Rs.' in i['item_price']:
                item.update({'symbol': 'Rs. '})
                total += updated_price
            order.append(item)
    return order, str(total)
