# Generated by Django 2.2 on 2020-02-27 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shippingAddress',
            new_name='shippingAddress1',
        ),
    ]
