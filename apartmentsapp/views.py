# from django.shortcuts import render, HttpResponse, redirect
# from django.views.generic import ListView
import datetime
from django.views.generic import ListView
from .models import Apartment


class AppListView(ListView):
    """ The landing page with offer of the apartments """
    model = Apartment
    template_name = 'index.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_update'] = datetime.datetime.now()
        return context

    









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

