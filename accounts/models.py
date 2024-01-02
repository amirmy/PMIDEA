from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
from django.db.models.signals import post_save


class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True, blank=False)
    name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined = models.DateField(auto_now_add=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} dashboard'


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Dashboard(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)
