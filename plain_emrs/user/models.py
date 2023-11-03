from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission

class CustomUser(AbstractUser):
    username = models.CharField(max_length=75, primary_key=True, null=False, blank=False)
    email_address = models.CharField(max_length=254, default="No email", null=False, blank=True)
    enabled = models.BooleanField(default=False, null=False)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    # Add a related_name to prevent conflicts
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='customuser_set')
    
