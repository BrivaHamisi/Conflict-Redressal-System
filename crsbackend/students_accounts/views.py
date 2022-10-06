from django.shortcuts import render, HttpResponse
from .models import ComplaintsForm, RegistrationForm
from .serializers import ComplaintsFormSerializer, UserSerializer, RegisterSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from . import models
 
class ComplaitsListViewset(viewsets.ModelViewSet):
	queryset = ComplaintsForm.objects.all()
	serializer_class = ComplaintsFormSerializer
	authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RegisterViewSet(viewsets.ModelViewSet):
	queryset = RegistrationForm.objects.all()
	serializer_class = RegisterSerializer
	
@csrf_exempt
def userlogin(request):
	email = request.POST['Email']
	password = request.POST['Password']
	userdata = models.RegistrationForm.objects.get(Email = email, Password = password)

	if userdata:
		return JsonResponse({'bool':True, 'userId':userdata.id})
	else:
		return(JsonResponse({'bool':False}))

	


# class ComplaintsList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
# 	queryset = ComplaintsForm.objects.all()
# 	serializer_class = ComplaintsFormSerializer

# 	def get(self, request):
# 		return self.list(request)
	
# 	def post(self, request):
# 		return self.create(request)
	

# class ComplaintsDetails(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
# 	queryset = ComplaintsForm.objects.all()
# 	serializer_class = ComplaintsFormSerializer

# 	lookup_field = 'id'

# 	def get(self, request, id):
# 		return self.retrieve(request, id=id)

	
# 	def put(self, request, id):
# 		return self.update(request, id=id)
	
# 	def delete(self, request, id):
# 		return self.destroy(request, id=id)

	



# Create your views here.
# @api_view(['GET', 'POST'])
# def AllComplaints_list(request):
# 	if request.method == 'GET':
# 		allcomplaints = ComplaintsForm.objects.all()
# 		serializer = ComplaintsFormSerializer(allcomplaints, many=True)
# 		return Response(serializer.data,)

# 	elif request.method == 'POST':
# 		serializer = ComplaintsFormSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status = status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT','DELETE'])
# def complaints_details(request, pk):
# 	try:
# 		complaint = ComplaintsForm.objects.get(pk=pk)
	
# 	except ComplaintsForm.DoesNotExist:
# 		return Response(staus=status.HTTP_400_BAD_REQUEST)
	
# 	if request.method == 'GET':
# 		serializer = ComplaintsFormSerializer(complaint)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = ComplaintsFormSerializer(complaint, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		complaint.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
