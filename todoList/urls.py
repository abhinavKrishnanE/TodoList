from django.urls import path
from.views import ListTaks, ListTaskDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = "todoList"


urlpatterns = [
    path('tasklist/', ListTaks.as_view(), name = "Listtask"),
    path('tasklist/<int:pk>/', ListTaskDetails.as_view(), name = "listtaskdetails"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]