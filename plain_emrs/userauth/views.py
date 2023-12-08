from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import AuthUser

class CustomUserCreateView(CreateView):
    model = AuthUser
    form_class = CustomUserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('user_created_success')