from django.db import models

from django.contrib.auth.models import AbstractUser 

from django.conf import settings

# Create your models here.


# ------------------------------------------------------- : Users Model 
class CrudUsers(AbstractUser):  
    #inheriting from AbstractUser, which have fields like :
    # username, first_name, last_name, email, password, is_active, is_staff, is_superuser, date_joined

    #additional features than AbstractUser
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='website/static/users_data/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username 
# ------------------------------------------------------- : Comments Model 
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to='website/static/users_data/post_images/', null=True, blank=True)
    video = models.FileField(upload_to='website/static/users_data/post_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.caption[:20]}'
    

# ------------------------------------------------------- : Likes Model 
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.post}'
    

# ------------------------------------------------------- : Message Model 

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.post}'

# -------------------------------------------------------   


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content}'

# -------------------------------------------------------
