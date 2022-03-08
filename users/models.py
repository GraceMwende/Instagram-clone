from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# resizing images
def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)
        
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_photo = models.ImageField(default='default.jpg',upload_to='media')
  bio = models.TextField()

  def __str__(self):
        return self.user.username

class Image(models.Model):
  image = models.ImageField(upload_to='images/', null=False)
  image_name = models.CharField(max_length=30)
  image_caption = models.CharField(max_length=30)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)