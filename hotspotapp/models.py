from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length=100)
    loc_image = models.ImageField(upload_to='location')

    def __str__(self):
        return self.loc_name

    class Meta:
        db_table = 'location'
        managed = True
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    
class Hotel(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lagos = models.BooleanField(default=False)
    abuja = models.BooleanField(default=False)
    owerri = models.BooleanField(default=False)
    enugu = models.BooleanField(default=False)
    ibadan = models.BooleanField(default=False)
    portharcourt = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='space', default ='pix.png', blank=True, null=True )
    details = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hotel'
        managed = True
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Showcase(models.Model):
    show_name = models.CharField(max_length=50)
    show_img = models.ImageField(upload_to='showcase', default='show.jpg')

    def __str__(self):
        return self.show_name
    
    class Meta:
        db_table = 'showcase'
        managed = True
        verbose_name = 'Showcase'
        verbose_name_plural = 'Showcases'
