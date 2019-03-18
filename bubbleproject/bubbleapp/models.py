from django.db import models

# Create your models here.

class Hashtag(models.Model):
    name = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=100)
    modified = models.DateTimeField('date modified', auto_now_add=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Beer(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField('beer name', max_length=200)
    abv = models.FloatField('Alcohol by volume')
    style = models.ForeignKey('Style', on_delete=models.PROTECT)
    isOrganic = models.BooleanField()
    isRetired = models.BooleanField()
    createDtae = models.DateField('Created')
    updateDate = models.DateField('Updated')
    glassName = models.CharField('Glass', max_length = 200)
    styleDescription = models.TextField('Description')

class Style(models.Model):
    id = models.CharField(primary_key=True)
    categoryName = models.ForeignKey('Category', on_delete=models.PROTECT)
    styleName = models.CharField(max_length=200)
    shortname =models.CharField(max_length=200)

class Category(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=200)
