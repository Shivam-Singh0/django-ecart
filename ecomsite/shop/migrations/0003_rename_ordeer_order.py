# Generated by Django 4.0.6 on 2022-08-04 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_ordeer_alter_products_discount_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ordeer',
            new_name='Order',
        ),
    ]
