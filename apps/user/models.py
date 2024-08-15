from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    ROLES = (
        ('admin', 'Администратор'),
        ('customer', 'Клиент'),
        ('seller', 'Продавец'),
    )
    role = models.CharField(max_length=100, null=True, blank=True, choices=ROLES)