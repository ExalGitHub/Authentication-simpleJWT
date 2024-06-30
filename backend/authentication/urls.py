from .views import CustomTokenObtainPairView, UsersListView, UserProfileView, UserCreateView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = (
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('user/create/', UserCreateView.as_view(), name='user'),
    path('user/profile/', UserProfileView.as_view(), name='user'),
    path('users/', UsersListView.as_view(), name='users'),
    
)
