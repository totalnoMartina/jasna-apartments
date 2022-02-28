from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def add_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = Photo()
            photo.caption = request.POST.get('caption')
            photo.save()
            return redirect('/photo/' + photo.id)
    else:
        form = PhotoForm()

    return render(request, 'add-photo.html', {'form': form})