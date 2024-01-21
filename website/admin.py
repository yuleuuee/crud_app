from django.contrib import admin
from .models import CrudUsers
from .models import Post

# Register your models here.

admin.site.register(CrudUsers)
admin.site.register(Post)

