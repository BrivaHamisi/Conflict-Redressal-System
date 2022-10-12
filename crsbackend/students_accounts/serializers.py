from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Complainant, Complaint, Feedback, Appeal


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
	class Meta:
		model = Complainant
		fields = '__all__'
		exclude = []


class ComplaintSerializer(serializers.ModelSerializer):
	class Meta:
		model = Complaint
		fields = '__all__'
		exclude = []


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