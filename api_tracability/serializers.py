from api_tracability.models import (
    Action,
    MiseEnCulture,
    NourrissageHumide,
    NourrissageSon,
    Tamisage,
    Recolte,
)
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "polymorphic_ctype", "recolte_nb", "column", "date"]


class MiseEnCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiseEnCulture
        fields = ["id", "recolte_nb", "column", "date"]


class NourrissageHumideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NourrissageHumide
        fields = [
            "id",
            "recolte_nb",
            "column",
            "date",
            "given_quantity",
            "given_quantity_bac",
            "marc_arrival_date",
            "anomaly",
            "anomaly_comment",
            "is_imw100_weighted",
            "imw100_weight",
        ]


class NourrissageSonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NourrissageSon
        fields = [
            "id",
            "recolte_nb",
            "column",
            "date",
            "given_quantity",
            "given_quantity_bac",
            "son_arrival_date",
        ]


class TamisageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamisage
        fields = ["id", "recolte_nb", "column", "date", "sieved_quantity"]


class RecolteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolte
        fields = ["id", "recolte_nb", "column", "date", "harvested_quantity"]


class ActionPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MiseEnCulture: MiseEnCultureSerializer,
        NourrissageHumide: NourrissageHumideSerializer,
        NourrissageSon: NourrissageSonSerializer,
        Tamisage: TamisageSerializer,
        Recolte: RecolteSerializer,
    }

    # def to_resource_type(self, model_or_instance):
    #     return model_or_instance._meta.object_name.lower()


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["column"]


class HarvestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["recolte_nb"]


class HistoricBreedingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "recolte_nb", "column", "date", "polymorphic_ctype"]
