from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Organization
from .models import User
from .models import Report
from .models import Interests


admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Report)
admin.site.register(Interests)




