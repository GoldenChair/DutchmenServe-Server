from django.contrib import admin

# Register your models here.
# from .models import Interest, Event, Organization, Registration, User, Report
# from .models import UserInterest, EventInterest, Membership, Leadership, Registration
from .models import Csgroups11112021, Csprojects11112021, Studentreportinglog11112021

admin.site.register(Studentreportinglog11112021)
admin.site.register(Csprojects11112021)
admin.site.register(Csgroups11112021)

# admin.site.register(Event)
# admin.site.register(Organization)
# admin.site.register(User)
# admin.site.register(Report)
# admin.site.register(Interest)
# admin.site.register(UserInterest)
# admin.site.register(EventInterest)
# admin.site.register(Membership)
# admin.site.register(Leadership)
# admin.site.register(Registration)