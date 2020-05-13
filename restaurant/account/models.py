from django.db import models

# Create your models here.


class OrderDetails(models.Model):
    oid = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('details.UserDetails', on_delete=models.CASCADE, related_name='customer_id')
    order_items = models.TextField()
    order_total = models.CharField(max_length=40)
    order_status = models.CharField(max_length=40)
    order_time = models.DateTimeField(auto_now=True)
    completion_time = models.DateTimeField(blank=True, null=True)
    manager_id = models.ForeignKey('details.UserDetails', related_name='manager_id', on_delete=models.CASCADE, blank=True, null=True)