from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Nie podano adresu email")
        if not username:
            raise ValueError("Nie podano username")
        if not first_name:
            raise ValueError("Nie podano imienia")
        if not last_name:
            raise ValueError("Nie podano nazwiska")
        if not phone_number:
            raise ValueError("Nie podano numeru telefonu")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone_number, password):
        user = self.create_user(
            self.normalize_email(email),
            username,
            first_name,
            last_name,
            phone_number,
            password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # basic staff
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="data joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # additional fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    # object set the manager
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # admin permissions
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        # user permissions
        return True
