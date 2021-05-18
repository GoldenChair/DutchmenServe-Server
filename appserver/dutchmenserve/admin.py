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