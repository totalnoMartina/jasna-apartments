from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView, View, DeleteView


class AppListView(View):
    """ The landing page with offer of the apartments """
    pass









# from .forms import PhotoForm
# from .models import Photo

# def add_photo(request):
#     """ A function to upload images """
#     if request.method == "POST":
#         form = PhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             photo = Photo()
#             photo.caption = request.POST.get('caption')
#             photo.save()
#             return redirect('/photo/' + photo.id)
#     else:
#         form = PhotoForm()

#     return render(request, 'add-photo.html', {'form': form})

