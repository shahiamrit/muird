from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Iru(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    par = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    photo1 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Vmgo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    par = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    par = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class Gallary(models.Model):
    img = models.ImageField(blank=True, null=True)
