# Generated by Django 3.2.3 on 2021-06-11 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]