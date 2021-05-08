from django.contrib import admin

# Register your models here.
from .models import Interest, Event, Organization, Registration, User, Report
from .models import UserInterest, EventInterest, Membership, Leadership, Registration

admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Report)
admin.site.register(Interest)
admin.site.register(UserInterest)
admin.site.register(EventInterest)
admin.site.register(Membership)
admin.site.register(Leadership)
admin.site.register(Registration)


# cd appserver
# python manage.py runserver 5455  #localhost or emulator
# python manage.py runserver 10.2.194.102:5455  #computer

# python manage.py migrate
# python manage.py makemigrations dutchmenserve  -- tell Django you made changes to models
# python manage.py sqlmigrate dutchmenserve #### -- prints to screen, check what Django will do
# python manage.py migrate -- rerun migrate to create tables/apply changes

# python manage.py createsuperuser -- create admin
# Username: admin
# Email address: admin@lvc.edu
# Password: dutchmenserve
