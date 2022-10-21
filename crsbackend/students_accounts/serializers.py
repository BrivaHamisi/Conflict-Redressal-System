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


# class ComplainantSerializer(serializers.ModelSerializer):
# 	username = serializers.CharField()
# 	email = serializers.EmailField()
# 	first_name = serializers.CharField()
# 	last_name = serializers.CharField()
# 	password = serializers.CharField()

# 	class Meta:
# 		depth = 1
# 		model = Complainant
# 		fields = '__all__'
# 		extra_kwargs = {
# 			'password': {
#                 'write_only': True,
#                 'required': True
#             },
# 			'username': {'read_only': False, 'required': True },
# 			'email': {'read_only': False, 'required': True },
# 			'first_name': {'read_only': False, 'required': True },
# 			'last_name': {'read_only': False, 'required': True },
# 			'user': {'read_only':True},
# 		}

# 	def get_username(self, obj):
# 		pass

# 	def create_user(self, data):
# 		username = data.get("username")
# 		email = data.get("email")
# 		first_name = data.get("first_name")
# 		last_name = data.get("last_name")
# 		password = data.get("password")
# 		user = None
# 		if username and email and first_name and last_name and password:
# 			user = User.objects.create(username=username, email=email, first_name=first_name, 
# 										last_name=last_name, password=password)
# 		return user

# 	def create(self, validated_data):
# 		username = validated_data["username"]
# 		email = validated_data["email"]
# 		first_name = validated_data["first_name"]
# 		last_name = validated_data["last_name"]
# 		password = validated_data["password"]
# 		del validated_data["username"]
# 		del validated_data["email"]
# 		del validated_data["first_name"]
# 		del validated_data["last_name"]
# 		del validated_data["password"]
# 		user = self.create_user({ "username":username, "email":email, "first_name":first_name, "last_name":last_name, "password":password })
# 		validated_data["user"] = user
# 		return super().create(validated_data)


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


class GeneralIssuesUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = GeneralIssuesUpdate
		fields = '__all__'
		exclude = []