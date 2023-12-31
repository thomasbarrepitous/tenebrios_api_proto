from django.db import models
from polymorphic.models import PolymorphicModel


class Action(PolymorphicModel):
    id = models.AutoField(primary_key=True)
    recolte_nb = models.CharField(max_length=6, default=None)
    column = models.CharField(max_length=2)
    date = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)


class MiseEnCulture(Action):
    pass


class NourrissageHumide(Action):
    given_quantity = models.FloatField()
    given_quantity_bac = models.FloatField()
    marc_arrival_date = models.DateTimeField()
    anomaly = models.BooleanField()
    anomaly_comment = models.TextField(blank=True, null=True)
    is_imw100_weighted = models.BooleanField()
    imw100_weight = models.FloatField(blank=True, null=True)


class NourrissageSon(Action):
    given_quantity = models.FloatField()
    given_quantity_bac = models.FloatField()
    son_arrival_date = models.DateTimeField()


class Tamisage(Action):
    sieved_quantity = models.FloatField()


class Recolte(Action):
    harvested_quantity = models.FloatField()
