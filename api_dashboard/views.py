from rest_framework import viewsets
from rest_framework import permissions
from api_dashboard.serializers import HumiditySerializer, TemperatureSerializer, CO2Serializer
from api_dashboard.models import Humidity, Temperature, CO2


class HumidityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
    permission_classes = [permissions.IsAuthenticated]


class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    permission_classes = [permissions.IsAuthenticated]


class C02ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CO2.objects.all()
    serializer_class = CO2Serializer
    permission_classes = [permissions.IsAuthenticated]
