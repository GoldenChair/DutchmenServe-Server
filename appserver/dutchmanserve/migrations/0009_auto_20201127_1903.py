# Generated by Django 3.1.2 on 2020-11-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutchmanserve', '0008_auto_20201127_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='emailAddress',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(to='dutchmanserve.Interests'),
        ),
    ]
