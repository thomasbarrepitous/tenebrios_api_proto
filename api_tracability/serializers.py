from api_tracability.models import Action
from rest_framework import serializers
import django_filters.rest_framework

class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["action_type", "column", "recolte_nb", "created_time", "uptime"]


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["column"]