from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('all_hotels', all_hotels, name='all_hotels'),
    path('locations', locations, name='locations'),
    path('location/<str:id>', single_location, name='location'),
    path('detail/<str:id>', detail, name='detail'),
    path('signout', signout, name='signout'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('profileupdate', profileupdate, name='profileupdate'),
    path('passwordupdate', passwordupdate, name='passwordupdate'),
]