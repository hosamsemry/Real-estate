from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager



class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_realtor(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_realtor = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_realtor = True
        user.save(using=self._db)

        return user
class UserAccount(AbstractUser, PermissionsMixin):

    username = None
    name = models.CharField(max_length=255,default='hosam')
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_realtor = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
