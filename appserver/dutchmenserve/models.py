from django.db import models

# Create your models here.

#Needs to be high up in code for relationships
class Interests(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'interests'

    def __str__(self):
        return self.name


#LVC Server Project/ Event on app
class Csprojects11112021(models.Model):
    projectid = models.AutoField(db_column='projectID',primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    eventdate = models.DateTimeField(db_column='eventDate', blank=True, null=True)

    class Meta:
        db_table = 'csProjects11112021'

#LVC Server Group/ Organization on app
class Csgroups11112021(models.Model):
    groupid = models.AutoField(db_column='groupID',primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grouptype = models.CharField(db_column='groupType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    subgroup = models.CharField(db_column='subGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.
    interests = models.ManyToManyField(Interests, null=True)
    class Meta:
        db_table = 'csGroups11112021'

    def __str__(self):
        return self.username

#LVC Student Reporting Log/ Report on app
# groupid and communityOrgid is thee same
class Studentreportinglog11112021(models.Model):
    logid = models.AutoField(db_column='logID',primary_key=True)  # Field name made lowercase.
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
        db_table = 'StudentReportingLog11112021'

class Users(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=4096, blank=True, null=True)
    interests = models.ManyToManyField(Interests, null=True)
    groups = models.ManyToManyField(Csgroups11112021, null=True)
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

