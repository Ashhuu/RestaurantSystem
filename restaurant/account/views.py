from django.shortcuts import render, redirect
from menu.views import retrieve_items
from menu import models as md
from details.models import UserDetails
from . import models
from datetime import datetime


# Create your views here.

def orderId(request, oid):
    row = models.OrderDetails.objects.get(oid=oid)
    row.order_time = row.order_time
    row.order_status = "Completed"
    row.manager_id = UserDetails.objects.get(username=request.user)
    row.completion_time = datetime.now()
    row.save()
    return redirect('order')

def orderDetails(request):
    menuItems = md.Menu.objects.all().values()
    order, total = retrieve_items(menuItems, request)
    itemsstring = getStringforDB(order)
    user = UserDetails.objects.get(username=request.user)
    if order != [] and total != 0:
        total = order[0]['symbol'] + total
        status = "Pending"
        order = models.OrderDetails(customer_id=user, order_items=itemsstring, order_total=total, order_status=status)
        order.save()

    orderDetails = models.OrderDetails.objects.filter(customer_id=user).values()
    orderDetails = modifyforHTML(orderDetails)
    if user.type == "manager":
        allOrders = models.OrderDetails.objects.all().values()
        allOrders = modifyforHTML(allOrders)
        pending = models.OrderDetails.objects.filter(order_status="Pending").exists()
        if pending:
            pendingExists = True
        else:
            pendingExists = False
        completed = models.OrderDetails.objects.filter(order_status="Completed").exists()
        if completed:
            completedExists = True
        else:
            completedExists = False
    else:
        allOrders = None
        pending = models.OrderDetails.objects.filter(customer_id=user, order_status="Pending").exists()
        if pending:
            pendingExists = True
        else:
            pendingExists = False
        completed = models.OrderDetails.objects.filter(customer_id=user, order_status="Completed").exists()
        if completed:
            completedExists = True
        else:
            completedExists = False

    return render(request, 'account/order.html', {'order': orderDetails, 'user': user, 'allOrders': allOrders,
                                                  'completed': completedExists, 'pending': pendingExists})


def modifyforHTML(orderDetails):
    for i in orderDetails:
        if i['order_status'].lower() == "pending":
            i.update({'color': 'red'})
        elif i['order_status'].lower() == "completed":
            i.update({'color': 'green'})
        i['order_items'] = i['order_items'].replace(';', ', ')[:-2]
    return orderDetails


def getStringforDB(orderDict):
    string = ''
    for item in orderDict:
        string += item['name'] + " x " + item['quantity'] + " qt;"
    return string
