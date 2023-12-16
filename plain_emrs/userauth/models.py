from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class AuthManager(BaseUserManager):
    def create_user(self, user_id, username, date_of_birth, email, first_name, last_name, password=None):
        if not user_id:
            raise ValueError("Users must have a user ID")

        user = self.model(
                user_id=user_id,
                username=username,
                date_of_birth=date_of_birth,
                email=email,
                first_name=first_name,
                last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, date_of_birth, first_name, last_name, password=None):
        user = self.create_user(
                user_id,
                password=password,
                date_of_birth=date_of_birth,
                email=email,
                first_name=first_name,
                last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class AuthUser(AbstractBaseUser):
    user_id = models.CharField(max_length=75, unique=True) 
    username = models.CharField(max_length=75)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(
            verbose_name="email address",
            max_length=255,
            unique=True,
    )
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    objects = AuthManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["username", "date_of_birth", "email", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

