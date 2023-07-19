from django.db import models

class Action(models.Model):
    class ActionType(models.TextChoices):
        NOURRISAGE_HUMIDE = 'NHUM'
        NOURRISAGE_SON = 'NSON'
        TAMISAGE = 'TAMI'
        RECOLTE = 'RECO'

    action_type = models.CharField(
        max_length=4,
        choices=ActionType.choices
    )
    column = models.CharField(
        max_length=2
    )
    recolte_nb = models.IntegerField()
    # created_time = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField()
    uptime = models.DateTimeField()
