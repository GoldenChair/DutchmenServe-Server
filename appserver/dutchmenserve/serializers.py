from rest_framework import serializers
# from .models import Event
# from .models import Organization
# from .models import User
# from .models import Report
# from .models import Interest
# from .models import Registration
# testing ones
from .models import Csprojects11112021
from .models import Csgroups11112021
from .models import Studentreportinglog11112021
# new models
# from .models import GroupInterests
from .models import Interests
# from .models import UserInterests
# from .models import UserGroups
from .models import Users


# Needs to be high up for other serializers
class InterestSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Interests
        fields = '__all__'

#testing one
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Csprojects11112021
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    class Meta:
        model = Csgroups11112021
        fields = '__all__'


class StudentReportingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentreportinglog11112021
        fields = '__all__'
#End of tesing ones

# New Models



class UserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    groups = GroupSerializer(many=True)
    class Meta:
        model = Users
        fields = '__all__'

# class UserGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserGroups
#         fields = '__all__'

# class UsersInterestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInterests
#         fields = '__all__'

# class GroupInterestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupInterests
#         fields = '__all__'

# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'

# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organization
#         fields = '__all__'

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = '__all__'

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Report
#         fields = '__all__'

# # class InterestSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Interest
# #         fields = '__all__'


# class RegistrationSerializer(serializers.ModelSerializer):
#     # user = UserSerializer()
#     # event = EventSerializer()
#     # success = serializers.BooleanField()

#     # def create(self, validated_data):
#     #     return Registration.objects.create(**validated_data)

#     # def update(self, instance, validated_data):
#     #     instance.user = validated_data.get('user', instance.user)
#     #     instance.event = validated_data.get('event', instance.event)
#     #     instance.success = validated_data.get('success', instance.success)
#     #     instance.save()
#     #     return instance

#     class Meta:
#         model = Registration
#         fields = '__all__'