# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Studentreportinglog(models.Model):
    logid = models.AutoField(db_column='logID', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='studentID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    projectid = models.ForeignKey('Csprojects', models.DO_NOTHING, db_column='projectID', blank=True, null=True)  # Field name made lowercase.
    projectname = models.ForeignKey('Csprojects', models.DO_NOTHING, db_column='projectName', blank=True, null=True)  # Field name made lowercase.
    groupid = models.ForeignKey('Csgroups', models.DO_NOTHING, db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    communityorgid = models.ForeignKey('Csgroups', models.DO_NOTHING, db_column='communityOrgID', blank=True, null=True)  # Field name made lowercase.
    hoursreported = models.FloatField(db_column='hoursReported', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.DateTimeField(db_column='serviceDate', blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateTimeField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    residentialstatuseligible = models.BooleanField(db_column='ResidentialStatusEligible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentReportingLog'


class Studentreportinglog11112021(models.Model):
    logid = models.AutoField(db_column='logID')  # Field name made lowercase.
    studentid = models.IntegerField(db_column='studentID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID', blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    communityorgid = models.IntegerField(db_column='communityOrgID', blank=True, null=True)  # Field name made lowercase.
    hoursreported = models.FloatField(db_column='hoursReported', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.DateTimeField(db_column='serviceDate', blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateTimeField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    residentialstatuseligible = models.BooleanField(db_column='ResidentialStatusEligible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentReportingLog11112021'


class Studentreportinglogbackup(models.Model):
    logid = models.AutoField(db_column='logID')  # Field name made lowercase.
    studentid = models.IntegerField(db_column='studentID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID', blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    communityorgid = models.IntegerField(db_column='communityOrgID', blank=True, null=True)  # Field name made lowercase.
    hoursreported = models.FloatField(db_column='hoursReported', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.DateTimeField(db_column='serviceDate', blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateTimeField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StudentReportingLogBackup'


class Csgroups(models.Model):
    groupid = models.AutoField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grouptype = models.CharField(db_column='groupType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    subgroup = models.CharField(db_column='subGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'csGroups'


class Csgroups11112021(models.Model):
    groupid = models.AutoField(db_column='groupID')  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grouptype = models.CharField(db_column='groupType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    subgroup = models.CharField(db_column='subGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'csGroups11112021'


class Csprojects(models.Model):
    projectid = models.AutoField(db_column='projectID', primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', unique=True, max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'csProjects'


class Csprojects11112021(models.Model):
    projectid = models.AutoField(db_column='projectID')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'csProjects11112021'
