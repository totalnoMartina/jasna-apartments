from django.contrib import admin
from .models import Apartment, Booking, Person
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Apartment)
class AppAdmin(SummernoteModelAdmin):
    """ An object to be seen by the administrator when apartmnents are created """
    list_display = ('name', 'last_update', 'bedroom_nr', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name', 'last_update')
    summernote_fields = ('content')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ For admin to managfe bookings """
    list_display = ('apartment', 'booking_id', 'status', 'check_in', 'check_out')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
    

admin.site.register(Person)
