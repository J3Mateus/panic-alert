import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.common.models.base_model import BaseModel
from apps.cop.models import COP
from apps.role.models import Roles
from apps.school.models import School

# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self, email,phone,whatsapp,first_name,last_name,created_by=None,deleted_by=None, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()),
                          phone=phone,
                          whatsapp=whatsapp,
                          first_name=first_name,
                          last_name=last_name,
                          created_by=created_by,
                          deleted_by=deleted_by,
                          is_active=is_active,
                          is_admin=is_admin,
                        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email,phone,whatsapp, first_name,last_name, password=None):
        user = self.create_user(
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    phone = models.CharField(null=True,verbose_name='phone')
    whatsapp = models.CharField(null=True,verbose_name='whatsapp')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name="first name",max_length=200)
    last_name = models.CharField(verbose_name="last name",max_length=200)
    created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_users')
    deleted_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='deleted_users')
    school = models.ManyToManyField(School, related_name='users_school', related_query_name='school_user',
                                through='BaseUserSchool', through_fields=('base_user', 'school'))
    
    role = models.ManyToManyField(Roles, related_name='users_role', related_query_name='role_user',
                                through='BaseUserRoles', through_fields=('base_user', 'role'))
    cop = models.ManyToManyField(COP, related_name='users_cop', related_query_name='cop_user',
                                through='BaseUserCop', through_fields=('base_user', 'cop'))   
    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name','phone','whatsapp']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def is_staff(self):
        return self.is_admin

class BaseUserSchool(models.Model):
    uuid         = models.UUIDField(default=uuid.uuid4, primary_key=True)
    base_user    = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    school       = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        app_label = 'users'
        db_table = f'{app_label}_base_user_school'
        verbose_name = 'Escola do usuario'
        verbose_name_plural = 'Escolas dos usuarios'
        
class BaseUserRoles(models.Model):
    uuid         = models.UUIDField(default=uuid.uuid4, primary_key=True)
    base_user    = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    role         = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        app_label = 'users'
        db_table = f'{app_label}_base_user_roles'
        verbose_name = 'Função do usuario'
        verbose_name_plural = 'Função dos usuarios'

class BaseUserCop(models.Model):
    uuid         = models.UUIDField(default=uuid.uuid4, primary_key=True)
    base_user    = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    cop         = models.ForeignKey(COP, on_delete=models.CASCADE)

    class Meta:
        app_label = 'users'
        db_table = f'{app_label}_base_user_cop'
        verbose_name = 'Delegacia do usuario'
        verbose_name_plural = 'Delegacias dos usuarios'