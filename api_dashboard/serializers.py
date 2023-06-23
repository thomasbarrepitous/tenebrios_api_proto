from api_dashboard.models import Temperature, CO2, Humidity
from rest_framework import serializers


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ["value", "sensor_nb", "created_time", "uptime"]


class HumiditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Humidity
        fields = ["value", "sensor_nb", "created_time", "uptime"]


class CO2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CO2
        fields = ["value", "sensor_nb", "created_time", "uptime"]
