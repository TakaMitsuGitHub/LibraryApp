from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default="", null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 利用者用追加フィールド
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    borrowed_day = models.DateTimeField(
        blank=True,
        null=True,
    )
    # is_expired = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def is_user(self):
        return not self.is_staff and not self.is_superuser

    def is_admin(self):
        return self.is_staff


# 役割
class RoleModel(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField('PermissionModel')


# 権限
class PermissionModel(models.Model):
    name = models.CharField(max_length=255)