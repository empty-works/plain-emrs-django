from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import AuthUser
import datetime
from datetime import datetime
import secrets
import string

class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    this_year = datetime.today().year
    year_range = [x for x in range(this_year - 120, this_year + 1)]
    date_of_birth = forms.DateField(help_text="Enter date of birth", 
                                    label="Birth year: ", 
                                    widget=forms.SelectDateWidget(years=year_range))
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = AuthUser
        fields = ( 'email', 'first_name', 'last_name', 'date_of_birth', 'groups',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hide the password fields
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()

    def save(self, commit=True):
        # Generate random password
        generated_password = self.generate_password()
        # Set the password on the model instance
        user = super().save(commit=False)
        user.set_password(generated_password)
        if commit:
            user.save()
        return user

    def generate_password(self):
        # Define characters to include in the password
        password_characters = string.ascii_letters + string.digits
        # Generate password of a specified length
        password_length = 12
        generated_password = ''.join(secrets.choice(password_characters) for _ in range(password_length))
        return generated_password