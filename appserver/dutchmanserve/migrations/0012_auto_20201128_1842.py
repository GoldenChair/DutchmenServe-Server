# Generated by Django 3.1.2 on 2020-11-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutchmanserve', '0011_auto_20201128_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registered',
            field=models.ManyToManyField(blank=True, null=True, to='dutchmanserve.User'),
        ),
    ]