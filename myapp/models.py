from django.db import models

class Contact_Us(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    image =models.ImageField(upload_to="movie/")

    def __str__(self):
        return self.movie_name
    
class Serial(models.Model):
    serial_name = models.CharField(max_length=100)
    image =models.ImageField(upload_to="serial/")

    def __str__(self):
        return self.serial_name
    
class Advertisement(models.Model):
    advertisement_name = models.CharField(max_length=100)
    image =models.ImageField(upload_to="advertisement/")

    def __str__(self):
        return self.advertisement_name

class Web_series(models.Model):
    web_series_name = models.CharField(max_length=100)
    image =models.ImageField(upload_to="web_series/")

    def __str__(self):
        return self.web_series_name