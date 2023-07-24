from api_tracability.models import Action, MiseEnCulture, NourrisageHumide, NourrisageSon, Tamisage, Recolte
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer


class ActionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['recolte_nb',"column", "date"]


class MiseEnCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiseEnCulture
        fields = ['recolte_nb', "column", "date"]


class NourrisageHumideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NourrisageHumide
        fields = ['recolte_nb', "column", "date", "given_quantity", "marc_arrival_date",
                  "anomaly", "anomaly_comment", "is_imw100_weighted", "imw100_weight"]


class NourrisageSonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NourrisageSon
        fields = ['recolte_nb', "column", "date",
                  "given_quantity", "son_arrival_date"]


class TamisageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamisage
        fields = ['recolte_nb', "column", "date", "sieved_quantity"]


class RecolteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolte
        fields = ['recolte_nb', "column", "date", "harvested_quantity"]


class ActionPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        MiseEnCulture: MiseEnCultureSerializer,
        NourrisageHumide: NourrisageHumideSerializer,
        NourrisageSon: NourrisageSonSerializer,
        Tamisage: TamisageSerializer,
        Recolte: RecolteSerializer
    }

    # def to_resource_type(self, model_or_instance):
    #     return model_or_instance._meta.object_name.lower()


class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ["column"]
