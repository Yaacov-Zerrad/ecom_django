# Generated by Django 4.0 on 2022-06-23 09:22

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0004_rename_desription_product_description'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('product', django.db.models.manager.Manager()),
            ],
        ),
    ]
