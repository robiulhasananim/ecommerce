from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import LogoutAPIView,RegisterAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    # login 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
