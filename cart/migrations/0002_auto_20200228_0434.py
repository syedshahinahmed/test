# Generated by Django 3.0.3 on 2020-02-28 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='ShoppingCart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='ShppoingCartItem',
        ),
    ]
