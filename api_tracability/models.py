from django.db import models
from polymorphic.models import PolymorphicModel


class Action(PolymorphicModel):
    recolte_nb = models.CharField(
        max_length=5,
        default=None
    )
    column = models.CharField(
        max_length=2
    )
    date = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    

class MiseEnCulture(Action):
    pass


class NourrisageHumide(Action):
    given_quantity = models.IntegerField()
    marc_arrival_date = models.DateTimeField()
    anomaly = models.BooleanField()
    anomaly_comment = models.TextField(blank=True)
    is_imw100_weighted = models.BooleanField()
    imw100_weight = models.IntegerField(blank=True)


class NourrisageSon(Action):
    given_quantity = models.IntegerField()
    son_arrival_date = models.DateTimeField()


class Tamisage(Action):
    sieved_quantity = models.IntegerField()


class Recolte(Action):
    harvested_quantity = models.IntegerField()

    
