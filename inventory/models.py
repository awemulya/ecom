from django.db import models


class Company(models.Model):
    name = models.CharField()


class Item(models.Model):
    name = models.CharField(max_length=256)
    rate = models.FloatField(null=True)
    company = models.ForeignKey(Company)

class OtherProperties(models.Model):
    item = models.ForeignKey(Item, related_name='properties')
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

class ItemImages(models.Model):
    item = models.ForeignKey(Item, related_name='images')
    file = models.ImageField()