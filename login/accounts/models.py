from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_RestaurantOwner=models.BooleanField(default=False)
    is_Customer=models.BooleanField(default=False)

    