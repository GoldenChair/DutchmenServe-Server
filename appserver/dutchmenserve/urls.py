from django.urls import path

from . import views
from .views import event_view
from .views import specific_event_view
from .views import org_view
from .views import specific_org_view
from .views import users_view
from .views import specific_users_view

from .views import specific_report_view
from .views import org_view
from .views import reports_view
from .views import interest_view
from .views import specific_interest


app_name = 'dutchmenserve'

urlpatterns = [
    path('events', views.event_view,name='all events'),
    path('event/<int:pk>/', views.specific_event_view,name='one event'),
    #org
    path('orgs', views.org_view,name='all orgs'),
    path('org/<int:pk>/', views.specific_org_view,name='one org'),
    #user
    path('users', views.users_view,name='all users'),
    path('user/<int:pk>/', views.specific_users_view,name='update user'),
    #report
    path('reports', views.reports_view,name='reports'),
    path('report/<int:pk>/', views.specific_report_view,name='specific report'),
    #interests
    path('interests', views.interest_view,name='get all or create a new interest'),
    path('interest/<int:pk>', views.specific_interest,name='get, edit, or delete a specific interest'),



    ##path('', views.index, name='index'),
]