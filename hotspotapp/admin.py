from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','loc_name','loc_image']
    list_editable = ['loc_name', 'loc_image']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id','location_id','location', 'name','image','lagos','abuja','owerri','enugu','ibadan','portharcourt']
    list_editable = ['name','image']


@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ['id','show_name','show_img']
    