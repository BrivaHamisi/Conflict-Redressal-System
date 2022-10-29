from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from students_accounts.views import (
    UserViewSet, ComplainantViewset, ComplaintViewset, FeedbackViewset, 
    AppealViewset, GeneralIssuesViewset, user_details
)
from knox import views as knox_views
from . import api


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('complainants', ComplainantViewset, basename='complainants')
router.register('complaints', ComplaintViewset, basename='complaints')
router.register('feedbacks', FeedbackViewset, basename='feedbacks')
router.register('appeals', AppealViewset, basename='appeals')
router.register('general_issues', GeneralIssuesViewset, basename='general_issues')
# router.register('user_details', user_details, basename='general_issues')
# router.register('token-auth', views.obtain_auth_token)

urlpatterns = [
    path('api/auth/login/', api.LoginAPI.as_view(), name='knox_login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/auth/register/', api.RegisterAPI.as_view(), name="register"),

    path('api/', include(router.urls)),
    path('api/user-details', user_details, name="user_details"),
]
