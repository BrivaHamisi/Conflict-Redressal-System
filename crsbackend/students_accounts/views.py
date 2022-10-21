from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Complainant, Complaint, Feedback, Appeal, GeneralIssuesUpdate
from .serializers import UserSerializer, ComplainantSerializer, ComplaintSerializer, FeedbackSerializer, AppealSerializer, GeneralIssuesUpdateSerializer


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


class GeneralIssuesViewset(viewsets.ModelViewSet):
	queryset = GeneralIssuesUpdate.objects.all()
	serializer_class = GeneralIssuesUpdateSerializer
	# authentication_classes = (TokenAuthentication,)


@api_view(['GET'])
@permission_classes(permissions.IsAuthenticated)
def user_details(request):
	usr = UserSerializer(request.user)
	return Response(usr.data)

