# Generated by Django 4.0 on 2022-06-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voiture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('qte', models.PositiveIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveIntegerField(blank=True, null=True)),
                ('cars', models.ManyToManyField(to='voiture.Cars')),
            ],
        ),
    ]
