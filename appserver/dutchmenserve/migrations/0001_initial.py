# Generated by Django 3.1.2 on 2021-05-08 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=100)),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('location', models.CharField(default='Lebanon Valley College', max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('isCommunity', models.BooleanField()),
                ('isResidential', models.BooleanField()),
                ('isOngoing', models.BooleanField()),
                ('imagepath', models.FileField(blank=True, null=True, upload_to='')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=30)),
                ('iconDataConstant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('imagepath', models.FileField(blank=True, null=True, upload_to='')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('emailAddress', models.EmailField(max_length=100)),
                ('events', models.ManyToManyField(blank=True, through='dutchmenserve.Registration', to='dutchmenserve.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.interest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(blank=True, through='dutchmenserve.UserInterest', to='dutchmenserve.Interest'),
        ),
        migrations.AddField(
            model_name='user',
            name='officer',
            field=models.ManyToManyField(blank=True, related_name='officer', through='dutchmenserve.Leadership', to='dutchmenserve.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(blank=True, through='dutchmenserve.Membership', to='dutchmenserve.Organization'),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagepath', models.FileField(blank=True, null=True, upload_to='')),
                ('deleted', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eid', to='dutchmenserve.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='dutchmenserve.user')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.user'),
        ),
        migrations.AddField(
            model_name='organization',
            name='officers',
            field=models.ManyToManyField(blank=True, through='dutchmenserve.Leadership', to='dutchmenserve.User'),
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='members', through='dutchmenserve.Membership', to='dutchmenserve.User'),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.user'),
        ),
        migrations.AddField(
            model_name='leadership',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.organization'),
        ),
        migrations.AddField(
            model_name='leadership',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.user'),
        ),
        migrations.CreateModel(
            name='EventInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.event')),
                ('interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dutchmenserve.interest')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='interests',
            field=models.ManyToManyField(blank=True, through='dutchmenserve.EventInterest', to='dutchmenserve.Interest'),
        ),
        migrations.AddField(
            model_name='event',
            name='registered',
            field=models.ManyToManyField(blank=True, through='dutchmenserve.Registration', to='dutchmenserve.User'),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('user', 'event')},
        ),
    ]
