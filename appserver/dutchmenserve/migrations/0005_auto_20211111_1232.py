# Generated by Django 3.2.8 on 2021-11-11 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dutchmenserve', '0004_auto_20211111_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='cretaedDate',
            new_name='createdDate',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='cretaedDate',
            new_name='createdDate',
        ),
    ]
