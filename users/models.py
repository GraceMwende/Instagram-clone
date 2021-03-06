from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
import PIL.Image
        
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_photo = models.ImageField(default='default.jpg',upload_to='media')
  bio = models.TextField()

  def __str__(self):
        return self.user.username

  # resizing images
  def save(self, *args, **kwargs):
      super().save()

      img = PIL.Image.open(self.profile_photo.path)
      

      if img.height > 100 or img.width > 100:
          new_img = (100, 100)
          img.thumbnail(new_img)
          img.save(self.profile_photo.path)
    
  def save_profile(self):
    self.save()


class Image(models.Model):
  image = models.ImageField(upload_to='images/', null=False)
  image_name = models.CharField(max_length=30)
  image_caption = models.CharField(max_length=30)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
    return self.image_name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def display_images(cls):
    img = cls.objects.all()
    return img