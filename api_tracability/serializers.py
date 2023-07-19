from api_tracability.models import Action
from rest_framework import serializers


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["action_type", "column", "recolte_nb", "created_time", "uptime"]