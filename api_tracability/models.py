from django.db import models


# Actions Enumeration
class ActionType(models.TextChoices):
    MISE_EN_CULTURE = 'CULT'
    NOURRISAGE_HUMIDE = 'NHUM'
    NOURRISAGE_SON = 'NSON'
    TAMISAGE = 'TAMI'
    RECOLTE = 'RECO'


class ActionDetail(models.Model):
    action_type_name = models.CharField(
        max_length=4,
        choices=ActionType.choices
    )
    column = models.CharField(
        max_length=2
    )
    date = models.DateTimeField()


class MiseCultureAction(models.Model):
    def __init__(self):
        self.action_name = ActionType.MISE_EN_CULTURE


class MarcAction(ActionDetail):
    def __init__(self):
        self.action_name = ActionType.NOURRISAGE_HUMIDE
    given_quantity = models.IntegerField()
    marc_arrival_date = models.DateTimeField()
    anomaly = models.BooleanField()
    anomaly_comment = models.TextField(default=None)
    is_imw100_weighted = models.BooleanField()
    imw100_weight = models.IntegerField(default=None)


class SonAction(ActionDetail):
    def __init__(self):
        self.action_name = ActionType.NOURRISAGE_SON
    given_quantity = models.IntegerField()
    son_arrival_date = models.DateTimeField()


class TamisageAction(ActionDetail):
    def __init__(self):
        self.action_name = ActionType.TAMISAGE
    sieved_quantity = models.IntegerField()


class RecolteAction(ActionDetail):
    def __init__(self):
        self.action_name = ActionType.RECOLTE
    harvested_quantity = models.IntegerField()


class Action(models.Model):
    action_detail = models.OneToOneField(ActionDetail, on_delete=models.CASCADE, default=None)
    column = models.CharField(
        max_length=2
    )
    recolte_nb = models.CharField(
        max_length=5
    )
    # For real-time tests
    # created_time = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField()
    uptime = models.DateTimeField()
