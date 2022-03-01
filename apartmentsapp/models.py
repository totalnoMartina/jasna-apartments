import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid 
# import cloudinary.uploader
# from django.db.models.signals import pre_delete
# import cloudinary

STATUS = ((0, "Available"), (1, "Occupied"), (2, "Pending"))


class Photo(models.Model):
    """ An image object to be uploaded """
    image = CloudinaryField('image')
    photo_id = models.CharField(max_length=7, unique=True)
    caption = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.caption if self.caption != "" else "No caption"
    
class Gallery(models.Model):
    """ Creating a Gallery for the apartments """
    photos = models.ManyToManyField('Photo', blank=True)

# class AppName(models.Model):
#     """ Using name to distinguish between apartments """
#     name = models.CharField(max_length=15, unique=True, blank=False)

#     def __str__(self):
#         return f'{self.name}'

class Apartment(models.Model):
    """ Main model of an apartment object """
    APP_NAMES = (('TONY', 'tony'), ('MATEA', 'matea'), ('MARTINA', 'martina'))
    name = models.CharField(max_length=10, choices=APP_NAMES)
    slug = models.SlugField(max_length=200, unique=True)
    bedroom_nr = models.IntegerField()
    sofa_bed = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_app')
    upload_image = CloudinaryField('image')
    more_images = CloudinaryField('another_image')
    last_update = models.DateField(auto_now=True)
    description = models.TextField(max_length=3000)
    
    def __str__(self):
        return f'{self.owner} has uploaded an offer of {self.name} apartment with {self.bedroom_nr} for the {self.price} price. '


class Booking(models.Model):
    """ An object to be accepted or denied by the owner """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, max_length=8)
    status = models.IntegerField(choices=STATUS, default=0)
    check_in = models.DateField()
    check_out = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}'



def check_availability(apartment, check_in, check_out):
    """ A function to check availability """
    avail_list = []
    booking_list = Booking.objects.filter(apartment=apartment)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()