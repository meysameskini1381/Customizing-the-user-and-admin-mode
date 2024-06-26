from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager


class UserManager(AbstractUserManager):
    def crate_user(self, phone_number, email, password=None, **extra_filds):
        if not phone_number or not email:
            raise ValueError('Users must have an email address')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email) , **extra_filds)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number,email , password=None, **extra_filds):
        extra_filds.setdefault('is_staff', True)
        extra_filds.setdefault('is_superuser', True)
        extra_filds.setdefault('is_admin', True)

        if extra_filds.get('is_staff') is not True:
            raise ValueError('is staff not True:')

        user = self.crate_user(phone_number,email, password=password, **extra_filds)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True,verbose_name='email',)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','username']

    objects = UserManager()

    def __str(self):
        return self.phone_number


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    address = models.TextField()
    postal_code = models.CharField(max_length=11)

    def __str__(self):
        return self.phone_number
