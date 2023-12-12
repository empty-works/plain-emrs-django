from django.urls import path
from .views import CustomUserCreateView, UserCreatedSuccessView

urlpatterns = [
        path('create_user/', CustomUserCreateView.as_view(), name='create-authuser'),
        path('user_created_success/', UserCreatedSuccessView.as_view(), name='user-created-success'),
]
