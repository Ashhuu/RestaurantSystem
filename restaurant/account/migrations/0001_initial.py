# Generated by Django 3.0.6 on 2020-05-13 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('order_items', models.TextField()),
                ('order_total', models.CharField(max_length=40)),
                ('order_status', models.CharField(max_length=40)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('completion_time', models.DateTimeField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to=settings.AUTH_USER_MODEL)),
                ('manager_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
