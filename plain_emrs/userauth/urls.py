from django.urls import path
from .views import CustomUserCreateView, UserCreatedSuccessView

urlpatterns = [
        path('create-authuser/', CustomUserCreateView.as_view(), name='create-authuser'),
        path('user-created-success/', UserCreatedSuccessView.as_view(), name='user-created-success'),
]
