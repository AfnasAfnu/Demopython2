# Generated by Django 4.1.1 on 2022-10-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]