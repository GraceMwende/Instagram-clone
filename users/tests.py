from django.test import TestCase

# Create your tests here.
from .models import Profile,Image

class ProfileTest(TestCase):
  def setUp(self):
    self.grace = Profile(bio='The best there is')
    

  #Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.grace,Profile))

  #Test Save method
  def test_save_category(self):
    self.grace.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

class ImageTestClass(TestCase):
  def setUp(self):
    # create new profile and save
    self.grace = Profile(bio='The best there is')
    self.save_profile()

    # create image instance
    self.new_image = Image(image_name='love',image_caption='sweet couple',profile=self.grace)
    self.new_image.save()

  def tearDown(self):
    Profile.objects.all.delete()
    Image.objects.all().delete()

  # test to display_images
  self.new_image = Image(image_name='love',image_caption='sweet couple',profile=self.grace)
  self.new_image.save()