from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FavouriteStyle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beerStyle = models.ForeignKey('Style', on_delete=models.CASCADE)
    modified = models.DateTimeField('date modified', auto_now_add=True)

    def __str__(self):
        return self.beerStyle

class FavouriteCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beerCategory = models.ForeignKey('Category', on_delete=models.CASCADE)
    modified = models.DateTimeField('date modified', auto_now_add=True)

    def __str__(self):
        return self.beerCategory

class Beer(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField('beer name', max_length=200)
    abv = models.FloatField('Alcohol by volume', default=None, null=True, blank=True)
    style = models.ForeignKey('Style', on_delete=models.PROTECT, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)
    isOrganic = models.BooleanField(blank=True, null=True)
    isRetired = models.BooleanField(blank=True, null=True)
    createDate = models.DateTimeField('Created', blank=True, null=True)
    updateDate = models.DateTimeField('Updated', blank=True, null=True)
    glassName = models.CharField('Glass', max_length = 200, blank=True)
    styleDescription = models.TextField('Description', blank=True)

    def __str__(self):
        return self.name

class Style(models.Model):
    styleName = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.styleName

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
