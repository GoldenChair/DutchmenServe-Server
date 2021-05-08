from django.urls import path

from . import views


app_name = 'dutchmenserve'

urlpatterns = [
    path('events', views.event_view,name='get all events'),
    path('event/<int:pk>', views.specific_event_view,name='get one event'),
    path('event/<int:eid>/register', views.registered_view, name='get list of registered for event'),
    path('event/<int:eid>/register/<int:uid>', views.register_view, name='post person for event or delete'),
    #org
    path('orgs', views.org_view,name='all orgs'),
    path('org/<int:pk>', views.specific_org_view,name='one org'),
    #user
    path('users', views.users_view,name='all users'),
    path('user/<int:pk>', views.specific_users_view,name='update user'),
    #report
    path('reports', views.reports_view,name='reports'),
    path('report/<int:pk>', views.specific_report_view,name='specific report'),
    path('reports/<int:pk>', views.all_reports_user, name='all reports for a user'),
    #interest
    path('interests', views.interest_view,name='get all or create a new interest'),
    path('interest/<int:pk>', views.specific_interest,name='get, edit, or delete a specific interest'),
]