from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from .models import AuthUser
import datetime
from datetime import datetime
import random

class CustomUserCreateView(CreateView):
    model = AuthUser
    form_class = CustomUserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('user_created_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        
        # Generate user ID
        user_id = self.generate_user_id(first_name, last_name)

        groups = form.cleaned_data['groups']
        self.object.groups.set(groups)
        # Save user with generated user ID
        form.instance.user_id = user_id
        return super().form_valid(form)
        #return response 

    # User ID generated by taking first and last name, current date and time, and a random number
    def generate_user_id(self, first_name, last_name):
        timestamp_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]  # Milliseconds
        random_number = str(random.randint(1000, 9999))
        user_id = f"{first_name.lower()}_{last_name.lower()}_{timestamp_str}_{random_number}"

        return user_id

class UserCreatedSuccessView(TemplateView):
    template_name = 'user_created_success.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'Successfully created a new user!'
        return context