# Generated by Django 4.2 on 2023-08-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpyou", "0005_product_card"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="delivery",
            field=models.CharField(default="3000", max_length=30),
        ),
    ]
