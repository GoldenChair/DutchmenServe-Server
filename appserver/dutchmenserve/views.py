from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer
from .models import Organization
from .serializers import OrganizationSerializer
from .models import User
from .serializers import UserSerializer
from .models import Report
from .serializers import ReportSerializer
from .models import Interest
from .serializers import InterestSerializer
from .models import Registration
from .serializers import RegistrationSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the dutchmenserve index.")

## EVENTS

##GET all events/ add a new event
@api_view(['GET', 'POST'])#Tested
def event_view(request):
    try:
        event_post = Event.objects.all()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EventSerializer(event_post, many = True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Get specific event and edit events, which includes editting the delete
@api_view(['GET', 'PUT'])#Tested and PUT can just take in the altered field
def specific_event_view(request, pk):
    try:
        event_post = Event.objects.get(id = pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EventSerializer(event_post, many = False)
        return Response(serializer.data)
    #PUT method to update 
    if request.method == 'PUT':
        serializer = EventSerializer(event_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#get all the users registered for an event, or register user for event
@api_view(['GET'])
def registered_view(request, eid):
    try:
        registrants = User.objects.filter(registration__event__id = eid)
    except Registration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(registrants, many = True)
        return Response(serializer.data)


#register user for event
@api_view(['PUT'])
def register_view(request, eid, uid):
    try:
        event_put = Event.objects.get(id = eid)
        user_put = User.objects.get(id = uid)
    except (Event.DoesNotExist or User.DoesNotExist) :
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'PUT':
    #     serializer = RegistrationSerializer(event_put, user_put, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        newRegistration = Registration(user = user_put, event = event_put)
        newRegistration.save()
        return Response(True, status=status.HTTP_201_CREATED)


###ORGANIZATIONS
#Get all organizations or create a new one
@api_view(['GET', 'POST'])#tested
def org_view(request):
    try:
        org_post = Organization.objects.all()
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrganizationSerializer(org_post, many = True)
        return Response(serializer.data)
    ##Create a new organization
    if request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get specific org
@api_view(['GET', 'PUT'])#Edit or get a specific org including editting the delete, tested
def specific_org_view(request, pk):
    try:
        org_post = Organization.objects.get(id = pk)
    except Organization.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrganizationSerializer(org_post, many = False)
        return Response(serializer.data)
    ##Put to edit specific org
    if request.method == 'PUT':
        serializer = OrganizationSerializer(org_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Users
##Get all users or create a new one
@api_view(['GET', 'POST'])
def users_view(request):
    try:
        user_post = User.objects.all()
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user_post, many = True)
        return Response(serializer.data)
    #Create a user
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Fetch a specific user
@api_view(['GET', 'PUT'])#Tested
def specific_users_view(request,pk):
    try:
        user_post = User.objects.get(id = pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user_post, many = False)
        return Response(serializer.data)
    #Edit a user, including ethe deleted

    if request.method == 'PUT':
        serializer = UserSerializer(user_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #update a user

## Report
##GET all reports or add a new one
@api_view(['GET', 'POST'])
def reports_view(request):
    try:
        report_post = Report.objects.all()
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReportSerializer(report_post, many = True)
        return Response(serializer.data)
    #Create a new report
    if request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Get specific report or edit a report
@api_view(['GET', 'PUT'])
def specific_report_view(request, pk):
    try:
        report_post = Report.objects.get(id = pk)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Get a specific report
    if request.method == 'GET':
        serializer = ReportSerializer(report_post, many = False)
        return Response(serializer.data)
    #edit a specific report or delete
    if request.method == 'PUT':
        serializer = ReportSerializer(report_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##Interest
@api_view(['GET','POST'])##Get all the interest or create a new one
def interest_view(request):
    try:
        interest_item = Interest.objects.all()
    except Interest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InterestSerializer(interest_item, many = True)
        return Response(serializer.data)
    #Create a new report
    if request.method == 'POST':
        serializer = InterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def specific_interest(request, pk):
    try:
        int_item = Interest.objects.get(id = pk)
    except Interest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Get a specific report
    if request.method == 'GET':
        serializer = InterestSerializer(int_item, many = False)
        return Response(serializer.data)
    #edit a specific report or delete
    if request.method == 'PUT':
        serializer = InterestSerializer(int_item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete an interest
    if request.method == 'DELETE':
        int_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
