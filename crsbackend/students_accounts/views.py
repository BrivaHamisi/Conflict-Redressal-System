from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

from .models import Complainant, Complaint, Feedback, Appeal
from .serializers import UserSerializer, ComplainantSerializer, ComplaintSerializer, FeedbackSerializer, AppealSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# authentication_classes = (TokenAuthentication,)

	def list(self, request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)


class ComplainantViewset(viewsets.ModelViewSet):
	queryset = Complainant.objects.all()
	serializer_class = ComplainantSerializer
	# authentication_classes = (TokenAuthentication,)
 

class ComplaintViewset(viewsets.ModelViewSet):
	queryset = Complaint.objects.all()
	serializer_class = ComplaintSerializer
	# authentication_classes = (TokenAuthentication,)


class FeedbackViewset(viewsets.ModelViewSet):
	queryset = Feedback.objects.all()
	serializer_class = FeedbackSerializer
	# authentication_classes = (TokenAuthentication,)


class AppealViewset(viewsets.ModelViewSet):
	queryset = Appeal.objects.all()
	serializer_class = AppealSerializer
	# authentication_classes = (TokenAuthentication,)

