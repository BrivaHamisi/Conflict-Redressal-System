from requests import request
from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Complainant, Complaint, Feedback, Appeal, GeneralIssuesUpdate

class UserSerializer(serializers.ModelSerializer):
	is_admin = serializers.SerializerMethodField("get_is_admin")

	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_admin']

		extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            },
			'is_staff': {'read_only':True}
        }

	def get_is_admin(self, obj):
		return obj.is_superuser

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user = user)
		return user


class ComplainantSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		depth = 1
		model = Complainant
		fields = '__all__'
	
	def create(self, validated_data):
		user = validated_data.pop("user")
		instance = User.objects.create_user(**user)
		validated_data["user"] = instance
		return super().create(validated_data)


class ComplaintSerializer(serializers.ModelSerializer):
	complainant = serializers.SerializerMethodField("get_complainant", read_only=True)

	class Meta:
		model = Complaint
		fields = '__all__'
		extra_kwargs = {
            'user': {
                'write_only': True,
            },
        }

	def create(self, validated_data):
		user = validated_data.pop("user")
		if type(user) == Complainant:
			pass
		elif type(user) in (int, str):
			print(user)
			user = Complainant.objects.get(user__id=int(user))
			print(user)
		validated_data["user"] = user
		return super().create(validated_data)

	def get_complainant(self, obj):
		if obj.user is None:
			return None
		return ComplainantSerializer(obj.user).data



class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback
		fields = '__all__'
		exclude = []

	
class AppealSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appeal
		fields = '__all__'
		exclude = []


class GeneralIssuesUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = GeneralIssuesUpdate
		fields = '__all__'
		exclude = []


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class LoggedinUser(serializers.ModelSerializer):
	user = ComplainantSerializer()
	fields = '__all__'
	