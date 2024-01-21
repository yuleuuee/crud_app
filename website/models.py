from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser 

class CrudUsers(AbstractUser):  
    #inheriting from AbstractUser, which have fields like :
    # username, first_name, last_name, email, password, is_active, is_staff, is_superuser, date_joined

    #additional features than AbstractUser
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username 