from django.db import models

# Create your models here.


class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.CharField(max_length=10)
    item_desc = models.TextField()
    item_img = models.ImageField(upload_to='menu/static/img')
    special = models.BooleanField(default=False)