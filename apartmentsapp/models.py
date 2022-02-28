from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.db.models.signals import pre_delete
import cloudinary

STATUS = ((0, "Available"), (1, "Occupied"), (2, "Pending"))


class Photo(models.Model):

    image = CloudinaryField('image')
    caption = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.caption if self.caption != "" else "No caption"


class Gallery(models.Model):
    photos = models.ManyToManyField('Photo', blank=True)


class Apartment(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    bedroom_nr = models.IntegerField()
    sofa_bed = models.BooleanField( default=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_app')
    upload_image = CloudinaryField('image')
    last_update = models.DateField(auto_now=True)
    description = models.TextField(max_length=3000)
    

