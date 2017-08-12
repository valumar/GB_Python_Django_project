from django.db import models


class MainService(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=250)
    fa_icon = models.CharField(max_length=12)
    bg_color = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=250)
    category = models.ForeignKey('MainService')
    price = models.DecimalField(max_digits=8, decimal_places=2)

