# Generated by Django 4.0 on 2022-06-22 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achetteur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('code', models.CharField(blank=True, max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achetteur.buyers')),
            ],
        ),
    ]
