from django.db import models
from django import utils


class Temperature(models.Model):
    value = models.FloatField()
    sensor_nb = models.IntegerField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField()
    uptime = models.DateTimeField()


class Humidity(models.Model):
    value = models.FloatField()
    sensor_nb = models.IntegerField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField()
    uptime = models.DateTimeField()


class CO2(models.Model):
    value = models.FloatField()
    sensor_nb = models.IntegerField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField()
    uptime = models.DateTimeField()
