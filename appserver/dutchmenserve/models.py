from django.db import models

# Create your models here.


class Interest(models.Model):
    interest = models.CharField(max_length = 30)
    def __str__(self):
        return self.interest


#User models 
class User(models.Model):
    #user_id = models.AutoField() ## we don't want autofield, but take one provided by DB
    firstName = models.CharField(max_length = 40)
    lastName = models.CharField(max_length = 40)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 50)
    emailAddress = models.EmailField(max_length = 100)
    interests = models.ManyToManyField(Interest, blank = True)
    events = models.ManyToManyField('Event', on_delete=models.CASCADE, blank=True)
    organizations = models.ManyToManyField('Organization', on_delete=models.CASCADE, blank=True)
    favorites = models.ManyToManyField('Event', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    #event_id = models.AutoField(primary_key =True)
    eventName = models.CharField(max_length=100)
    date = models.DateTimeField('Date', null = True)
    location = models.CharField(max_length = 100, default = 'Lebanon Valley College')
    description = models.TextField(max_length=500)
    interests = models.ManyToManyField(Interest, blank = True)
    isCommunity = models.BooleanField()
    isResidential = models.BooleanField()
    isOngoing = models.BooleanField()
    imagepath = models.FileField(null = True, blank = True)
    registered = models.ManyToManyField(User, blank = True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.eventName

class Organization(models.Model):
    ##org_id = models.AutoField
    orgName = models.CharField(max_length = 40)
    description = models.TextField(max_length=500)
    email = models.EmailField(max_length = 254, blank = True, null=True)
    officers = models.ManyToManyField(User, blank=True)
    users = models.ManyToManyField(User, related_name='members', blank=True)
    imagepath = models.FileField(blank= True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.orgName

class Report(models.Model):
    event = models.ForeignKey(Event, related_name='eid', on_delete= models.CASCADE)
    hours = models.DecimalField(decimal_places=2, max_digits=5)
    user = models.ForeignKey(User, related_name='uid', on_delete=models.CASCADE)
    #report_id
    additional = models.ManyToManyField(User, blank = True)
    imagepath = models.FileField(blank= True, null = True)
    deleted = models.BooleanField(default=False)
     
