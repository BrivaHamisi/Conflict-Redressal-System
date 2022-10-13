from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from students_accounts.views import UserViewSet, ComplainantViewset, ComplaintViewset, FeedbackViewset, AppealViewset, GeneralIssuesViewset

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('complainants', ComplainantViewset, basename='complainants')
router.register('complaints', ComplaintViewset, basename='complaints')
router.register('feedbacks', FeedbackViewset, basename='feedbacks')
router.register('appeals', AppealViewset, basename='appeals')
router.register('general_issues', GeneralIssuesViewset, basename='general_issues')
# router.register('token-auth', views.obtain_auth_token)

urlpatterns = [
    path('api/', include(router.urls)),
]
