# Generated by Django 3.2.9 on 2021-12-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutchmenserve', '0002_auto_20211212_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(null=True, to='dutchmenserve.Csgroups11112021'),
        ),
        migrations.AlterField(
            model_name='users',
            name='interests',
            field=models.ManyToManyField(null=True, to='dutchmenserve.Interests'),
        ),
    ]
