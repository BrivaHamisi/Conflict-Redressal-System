from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated   

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from .models import Complainant, Complaint, Feedback, Appeal, GeneralIssuesUpdate
from .serializers import UserSerializer, ComplainantSerializer, ComplaintSerializer, FeedbackSerializer, AppealSerializer, GeneralIssuesUpdateSerializer, ChangePasswordSerializer
from .filters import *


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

    def get_queryset(self):
        curr_user = self.request.query_params.get("current_user")
        user_id = self.request.query_params.get("user_id")
        queryset = Complaint.objects.all()
        if curr_user is not None:
            queryset = queryset.filter(user__user__id=self.request.user.id)
        elif user_id is not None:
            queryset = queryset.filter(user__user__id=user_id)

        return queryset

    def create(self, request, *args, **kwargs):
        uid = request.data.get("user")
        if type(uid) == int:
            complainant = Complainant.objects.get(user__id=uid)
            request.data["user"] = complainant.id
        return super().create(request, *args, **kwargs)


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


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoggedinUserView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ComplainantSerializer
    queryset = get_user_model().objects.all()


def sendEmails(request, title='Complaint Successfully Submitted', body='Email content'):
    email = EmailMessage(
        title,
        body,
        settings.EMAIL_HOST_USER,
        [request.user.email, "nivleknatech@gmail.com"],
    )
    email.fail_silently= False
    email.send()


