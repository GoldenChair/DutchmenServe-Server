from django.db import models

# Create your models here.

#LVC Server Project/ Event on app
class Csprojects11112021(models.Model):
    projectid = models.AutoField(db_column='projectID',primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    reviewdate = models.DateTimeField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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

    class Meta:
        managed = False
        db_table = 'csGroups11112021'

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
        managed = False
        db_table = 'StudentReportingLog11112021'

# class Interest(models.Model):  #add id
#     interest = models.CharField(max_length = 30)
#     iconDataConstant = models.IntegerField()
#     color = models.CharField(max_length=10)
#     fillColor = models.CharField(max_length=10)
    
#     def __str__(self):
#         return self.interest


# #User models 
# class User(models.Model):
#     #user_id = models.AutoField() ## we don't want autofield, but take one provided by DB
#     firstName = models.CharField(max_length = 40)
#     lastName = models.CharField(max_length = 40)
#     username = models.CharField(max_length = 20)
#     password = models.CharField(max_length = 50)
#     emailAddress = models.EmailField(max_length = 100)
#     interests = models.ManyToManyField(Interest, blank = True, through='UserInterest')   
#     events = models.ManyToManyField('Event',  blank=True, through='Registration')   
#     organizations = models.ManyToManyField('Organization', blank=True, through='Membership')   
#     officer = models.ManyToManyField('Organization', blank=True, related_name='officer', through='Leadership')

#     def __str__(self):
#         return self.username

# class Event(models.Model):
#     #event_id = models.AutoField(primary_key =True)
#     eventName = models.CharField(max_length=100)
#     date = models.DateTimeField('Date', null = True)
#     location = models.CharField(max_length = 100, default = 'Lebanon Valley College')
#     description = models.TextField(max_length=500)
#     interests = models.ManyToManyField(Interest, blank = True, through='EventInterest')  
#     isCommunity = models.BooleanField()
#     isResidential = models.BooleanField()
#     isOngoing = models.BooleanField()
#     imagepath = models.FileField(null = True, blank = True)
#     registered = models.ManyToManyField(User, blank = True, through='Registration')   
#     deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.eventName

# class Organization(models.Model):
#     ##org_id = models.AutoField
#     orgName = models.CharField(max_length = 40)
#     description = models.TextField(max_length=500)
#     email = models.EmailField(max_length = 254, blank = True, null=True)
#     officers = models.ManyToManyField(User, blank=True, through='Leadership')   
#     users = models.ManyToManyField(User, related_name='members', blank=True, through='Membership')   
#     imagepath = models.FileField(blank= True, null=True)
#     deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.orgName

# class Report(models.Model):
#     event = models.ForeignKey(Event, related_name='eid', on_delete= models.CASCADE)
#     hours = models.DecimalField(decimal_places=2, max_digits=5)
#     user = models.ForeignKey(User, related_name='uid', on_delete=models.CASCADE)
#     #report_id  
#     imagepath = models.FileField(blank= True, null = True)
#     deleted = models.BooleanField(default=False)
     
# class UserInterest(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     interest = models.ForeignKey(Interest, null=True, on_delete=models.SET_NULL)

# class EventInterest(models.Model):
#     event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
#     interest = models.ForeignKey(Interest, null=True, on_delete=models.SET_NULL)

# class Membership(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)

# class Leadership(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)

# class Registration(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#     event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
#     class Meta:
#         unique_together = ['user', 'event']
