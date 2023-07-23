from api_tracability.models import Action, ActionDetail, MiseCultureAction, MarcAction, SonAction, RecolteAction, TamisageAction
from rest_framework import serializers
import django_filters.rest_framework
from rest_polymorphic.serializers import PolymorphicSerializer


class ActionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionDetail
        fields = ["action_type_name", "column", "date"]


class MiseCultureActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiseCultureAction
        fields = ["action_type_name", "column", "date"]


class MarcActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcAction
        fields = ["action_type_name", "column", "date", "given_quantity", "marc_arrival_date",
                  "anomaly", "anomaly_comment", "is_imw100_weighted", "imw100_weight"]


class SonActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SonAction
        fields = ["action_type_name", "column", "date",
                  "given_quantity", "son_arrival_date"]


class TamisageActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamisageAction
        fields = ["action_type_name", "column", "date", "sieved_quantity"]


class RecolteActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecolteAction
        fields = ["action_type_name", "column", "date", "harvested_quantity"]


class ActionDetailPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MiseCultureAction: MiseCultureActionSerializer,
        MarcAction: MarcActionSerializer,
        SonAction: SonActionSerializer,
        TamisageAction: TamisageActionSerializer,
        RecolteAction: RecolteActionSerializer
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["action_detail", "column",
                  "recolte_nb", "created_time", "uptime"]


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["column"]
