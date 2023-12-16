from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import AuthUser
import datetime
from datetime import datetime

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
        fields = ('user_id', 'date_of_birth', 'email', 'first_name', 'last_name', 'groups',)