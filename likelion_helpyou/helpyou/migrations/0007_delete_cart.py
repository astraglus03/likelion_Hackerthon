# Generated by Django 4.2 on 2023-08-02 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("helpyou", "0006_product_delivery"),
    ]

    operations = [
        migrations.DeleteModel(name="Cart",),
    ]
