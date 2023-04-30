from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, phone, password=None):
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            name = name,
            username = username,
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, phone, username ,password, name):
        user=self.create_user(
            name = name,
            username = username,
            password = password,
            phone = phone,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    role = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    username = models.TextField(max_length=50, null=False, unique=True)
    password = models.TextField(max_length=50)

    last_login = models.DateTimeField(auto_now_add=True)
    is_admin  = models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser   = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','phone']

    objects = MyAccountManager()

    def _str_(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True









    
