from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(_('email address'), unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  objects = CustomUserManager()


  def get_absolute_url(self):
    return reverse('user_detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.email
