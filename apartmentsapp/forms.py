from django import forms
from django.forms import ModelForm
from .models import  Photo, Gallery

class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields=['multipleimages']  
        label ={}
        widgets ={
            'multipleimages':forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True}),
        } 

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'caption')