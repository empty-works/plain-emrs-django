from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from .models import AuthUser

class CustomUserCreateView(CreateView):
    model = AuthUser
    form_class = CustomUserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('user_created_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        groups = form.cleaned_data['groups']
        self.object.groups.set(groups)
        return response 

class UserCreatedSuccessView(TemplateView):
    template_name = 'user_created_success.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'Successfully created a new user!'
        return context