from django.contrib import admin

# Register your models here.
from .models import Profile,Image

admin.site.register(Profile)
admin.site.register(Image)