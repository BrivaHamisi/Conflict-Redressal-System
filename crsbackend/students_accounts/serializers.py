from rest_framework import serializers 
from .models import ComplaintsForm, RegistrationForm
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class ComplaintsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintsForm
        fields = '__all__'
        # fields = ('id','Complain_description', 'Events_that_took_Place', 'Consequence_suffered', 'Spoken_to_someone','Dissatisfied_with_Informal_complaint','evidence', 'recommendation', 'date', 'status_of_complaint')


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']

		extra_kwargs= {
            'password':{
                'write_only':True,
                'required':True
            }
        }

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user = user)
		return user


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegistrationForm
		fields = ['id','RegNo', 'Course', 'Campus', 'Department', 'Phone_Number']