# Generated by Django 3.2.9 on 2021-12-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csgroups11112021',
            fields=[
                ('groupid', models.AutoField(db_column='groupID', primary_key=True, serialize=False)),
                ('groupname', models.CharField(blank=True, db_column='groupName', max_length=50, null=True)),
                ('grouptype', models.CharField(blank=True, db_column='groupType', max_length=25, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('subgroup', models.CharField(blank=True, db_column='subGroup', max_length=50, null=True)),
                ('approved', models.CharField(blank=True, max_length=1, null=True)),
                ('reviewdate', models.DateTimeField(blank=True, db_column='reviewDate', null=True)),
            ],
            options={
                'db_table': 'csGroups11112021',
            },
        ),
        migrations.CreateModel(
            name='Csprojects11112021',
            fields=[
                ('projectid', models.AutoField(db_column='projectID', primary_key=True, serialize=False)),
                ('projectname', models.CharField(db_column='projectName', max_length=50)),
                ('createddate', models.DateTimeField(blank=True, db_column='createdDate', null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('approved', models.CharField(blank=True, max_length=1, null=True)),
                ('reviewdate', models.DateTimeField(blank=True, db_column='reviewDate', null=True)),
            ],
            options={
                'db_table': 'csProjects11112021',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='Studentreportinglog11112021',
            fields=[
                ('logid', models.AutoField(db_column='logID', primary_key=True, serialize=False)),
                ('studentid', models.IntegerField(blank=True, db_column='studentID', null=True)),
                ('username', models.CharField(blank=True, db_column='userName', max_length=25, null=True)),
                ('projectid', models.IntegerField(blank=True, db_column='projectID', null=True)),
                ('projectname', models.CharField(blank=True, db_column='projectName', max_length=50, null=True)),
                ('groupid', models.IntegerField(blank=True, db_column='groupID', null=True)),
                ('communityorgid', models.IntegerField(blank=True, db_column='communityOrgID', null=True)),
                ('hoursreported', models.FloatField(blank=True, db_column='hoursReported', null=True)),
                ('servicedate', models.DateTimeField(blank=True, db_column='serviceDate', null=True)),
                ('submissiondate', models.DateTimeField(blank=True, db_column='submissionDate', null=True)),
                ('approved', models.CharField(blank=True, max_length=1, null=True)),
                ('reviewdate', models.DateTimeField(blank=True, db_column='reviewDate', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('residentialstatuseligible', models.BooleanField(blank=True, db_column='ResidentialStatusEligible', null=True)),
            ],
            options={
                'db_table': 'StudentReportingLog11112021',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('token', models.CharField(blank=True, max_length=4096, null=True)),
                ('groups', models.ManyToManyField(to='dutchmenserve.Csgroups11112021')),
                ('interests', models.ManyToManyField(to='dutchmenserve.Interests')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='csgroups11112021',
            name='interests',
            field=models.ManyToManyField(to='dutchmenserve.Interests'),
        ),
    ]
