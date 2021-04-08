from rest_framework import serializers
from .models import Event
from .models import Organization
from .models import User
from .models import Report
from .models import Interest
from .models import Registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # event = EventSerializer()
    # success = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Registration.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.event = validated_data.get('event', instance.event)
    #     instance.success = validated_data.get('success', instance.success)
    #     instance.save()
    #     return instance

    class Meta:
        model = Registration
        fields = '__all__'