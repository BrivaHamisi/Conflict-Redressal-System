from django.urls import path,include
from students_accounts.views import ComplaitsListViewset, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('complaints', ComplaitsListViewset, basename='complaints')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('complaints/', ComplaintsList.as_view()),
    # path('complaints/<int:id>/', ComplaintsDetails.as_view()),

    # path('complaints', AllComplaints_list),
    # path('complaints/<int:pk>/', complaints_details),

]