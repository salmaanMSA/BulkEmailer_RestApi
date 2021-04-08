from django.db import models
from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .registeration_models import AdminRegisteration


class UserManager(BaseUserManager):
    """
        Custom User Manager
    """

    def create_user(self,email=str, password=str, **extra_fields):
        """
            Create Normal User
        :return: string
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email=str, password=str, **extra_fileds):

        """
            Create Super User
        :param email:
        :param password:
        :param extra_fileds:
        :return:string
        """

        extra_fileds.setdefault("is_staff", True)
        extra_fileds.setdefault("is_superuser", True)
        extra_fileds.setdefault("is_active", True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError(_("Super user must have is_superuser=True."))
        return self.create_user(email)



class CustomUser(AbstractBaseUser):
    """
        Custom User Table Desc
    """

    id = models.UUIDField(default=uuid4, primary_key=True)
    ref_id = models.ForeignKey(to=AdminRegisteration, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="Email-ID", max_length=155, unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
