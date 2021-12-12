import io
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# from .models import Event
# from .serializers import EventSerializer
from .models import Csgroups11112021, Interests, Users
from .serializers import GroupSerializer, InterestSerializer, UserSerializer
from .models import Csprojects11112021
from .serializers import ProjectSerializer
from .models import Studentreportinglog11112021
from .serializers import StudentReportingLogSerializer

# from .models import Organization
# from .serializers import OrganizationSerializer
# from .models import User
# from .serializers import UserSerializer
# from .models import Report
# from .serializers import ReportSerializer
# from .models import Interest
# from .serializers import InterestSerializer
# from .models import Registration
# from .serializers import RegistrationSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the dutchmenserve index.")

## EVENTS

##GET all events/ add a new event
@api_view(['GET', 'POST'])#Tested
def event_view(request):
    try:
        event_post = Csprojects11112021.objects.all()
    except Csprojects11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProjectSerializer(event_post, many = True)
    return Response(serializer.data)

#Get specific event and edit events, which includes editting the delete
@api_view(['GET', 'PUT'])#Tested and PUT can just take in the altered field
def specific_event_view(request, pk):
    try:
        event_post = Csprojects11112021.objects.get(projectid = pk)
    except Csprojects11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #PUT method to update 
    if request.method == 'PUT':
        serializer = ProjectSerializer(event_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #GET by default
    serializer = ProjectSerializer(event_post, many = False)
    return Response(serializer.data)

###ORGANIZATIONS
#Get all organizations or create a new one
@api_view(['GET', 'POST'])
def org_view(request):
    try:
        org_post = Csgroups11112021.objects.all()
    except Csgroups11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = GroupSerializer(org_post, many = True)
    return Response(serializer.data)

#Get specific org
@api_view(['GET', 'PUT'])
def specific_org_view(request, pk):
    try:
        org_post = Csgroups11112021.objects.get(groupid = pk)
    except Csgroups11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = GroupSerializer(org_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = GroupSerializer(org_post, many = False)
    return Response(serializer.data)

## Report
##GET all reports or add a new one
@api_view(['GET', 'POST'])
def reports_view(request):
    try:
        report_post = Studentreportinglog11112021.objects.all()
    except Studentreportinglog11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = StudentReportingLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = StudentReportingLogSerializer(report_post, many = True)
    return Response(serializer.data)

#Get specific report or edit a report
@api_view(['GET', 'PUT'])
def specific_report_view(request, pk):
    try:
        report_post = Studentreportinglog11112021.objects.get(logid = pk)
    except Studentreportinglog11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentReportingLogSerializer(report_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = StudentReportingLogSerializer(report_post, many = False)
    return Response(serializer.data)


#Get all reports for a user
@api_view(['GET'])
def all_reports_user(request, pk):
    try: 
        reports_for_user = Studentreportinglog11112021.objects.filter(user = pk)
    except Studentreportinglog11112021.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentReportingLogSerializer(reports_for_user, many=True)
    return Response(serializer.data)

## interests

#Get all interests or post new one
@api_view(['GET', 'POST'])
def interests_view(request):
    try:
        interests = Interests.objects.all()
    except Interests.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = InterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = InterestSerializer(interests, many = True)
    return Response(serializer.data)

#Get interests for a user or post a new interest for a user
#TODO
# @api_view(['GET', 'PUT'])
# def specific_interest(request, pk):
#     try:
#         User = Users.objects.get(id = pk)
#     except InterestSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = InterestSerializer(report_post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = InterestSerializer(report_post, many = False)
#     return Response(serializer.data)

## GET all users/ add a new user
#TODO not working
@api_view(['GET', 'POST'])#Tested
def users_view(request):
    try:
        user_post = Users.objects.all()
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = Users(user_post, many = True)
    return Response(serializer.data)

#Get specific user and edit user
#TODO needs testing with put
@api_view(['GET', 'PUT'])
def specific_users_view(request, pk):
    try:
        user_post = Users.objects.get(id = pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #PUT method to update 
    if request.method == 'PUT':
        serializer = UserSerializer(user_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #GET by default
    serializer = UserSerializer(user_post, many = False)
    return Response(serializer.data)

## EVENTS

# ##GET all events/ add a new event
# @api_view(['GET', 'POST'])#Tested
# def event_view(request):
#     try:
#         event_post = Event.objects.all()
#     except Event.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'POST':
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = EventSerializer(event_post, many = True)
#     return Response(serializer.data)

# #Get specific event and edit events, which includes editting the delete
# @api_view(['GET', 'PUT'])#Tested and PUT can just take in the altered field
# def specific_event_view(request, pk):
#     try:
#         event_post = Event.objects.get(id = pk)
#     except Event.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     #PUT method to update 
#     if request.method == 'PUT':
#         serializer = EventSerializer(event_post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #GET by default
#     serializer = EventSerializer(event_post, many = False)
#     return Response(serializer.data)


# #get all the users registered for an event, or register user for event
# @api_view(['GET'])
# def registered_view(request, eid):
#     try:
#         registrants = User.objects.filter(registration__event__id = eid)
#     except Registration.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = UserSerializer(registrants, many = True)
#     return Response(serializer.data)

# #register user for event
# @api_view(['POST', 'DELETE'])
# def register_view(request, eid, uid):
#     try:
#         event_post = Event.objects.get(id = eid)
#         user_post = User.objects.get(id = uid)
#     except Event.DoesNotExist or User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'POST':
#         newRegistration = Registration(user = user_post, event = event_post)
#         serializer = RegistrationSerializer(newRegistration)
#         content = JSONRenderer().render(serializer.data)
#         stream = io.BytesIO(content)
#         data = JSONParser().parse(stream)
#         serializer = RegistrationSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Registration.objects.filter(event__id = eid, user__id = uid).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ###ORGANIZATIONS
# #Get all organizations or create a new one
# @api_view(['GET', 'POST'])
# def org_view(request):
#     try:
#         org_post = Organization.objects.all()
#     except Organization.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'POST':
#         serializer = OrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = OrganizationSerializer(org_post, many = True)
#     return Response(serializer.data)

# #Get specific org
# @api_view(['GET', 'PUT'])
# def specific_org_view(request, pk):
#     try:
#         org_post = Organization.objects.get(id = pk)
#     except Organization.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         serializer = OrganizationSerializer(org_post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = OrganizationSerializer(org_post, many = False)
#     return Response(serializer.data)

# ## Users
# ##Get all users or create a new one
# @api_view(['GET', 'POST'])
# def users_view(request):
#     try:
#         user_post = User.objects.all()
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = UserSerializer(user_post, many = True)
#     return Response(serializer.data)
    
# #Fetch a specific user
# @api_view(['GET', 'PUT'])
# def specific_users_view(request,pk):
#     try:
#         user_post = User.objects.get(id = pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = UserSerializer(user_post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = UserSerializer(user_post, many = False)
#     return Response(serializer.data)

# ## Report
# ##GET all reports or add a new one
# @api_view(['GET', 'POST'])
# def reports_view(request):
#     try:
#         report_post = Report.objects.all()
#     except Report.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'POST':
#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = ReportSerializer(report_post, many = True)
#     return Response(serializer.data)

# #Get specific report or edit a report
# @api_view(['GET', 'PUT'])
# def specific_report_view(request, pk):
#     try:
#         report_post = Report.objects.get(id = pk)
#     except Report.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = ReportSerializer(report_post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = ReportSerializer(report_post, many = False)
#     return Response(serializer.data)


# #Get all reports for a user
# @api_view(['GET'])
# def all_reports_user(request, pk):
#     try: 
#         reports_for_user = Report.objects.filter(user = pk)
#     except Report.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     serializer = ReportSerializer(reports_for_user, many=True)
#     return Response(serializer.data)


# ##Interest
# @api_view(['GET','POST'])
# def interest_view(request):
#     try:
#         interest_item = Interest.objects.all()
#     except Interest.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'POST':
#         serializer = InterestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = InterestSerializer(interest_item, many = True)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def specific_interest(request, pk):
#     try:
#         int_item = Interest.objects.get(id = pk)
#     except Interest.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         serializer = InterestSerializer(int_item,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         int_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = InterestSerializer(int_item, many = False)
#     return Response(serializer.data)
