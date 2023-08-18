from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api_tracability.serializers import ColumnSerializer, ActionPolymorphicSerializer, HistoricBreedingsSerializer
from api_tracability.models import Action
from rest_framework.decorators import action as decorator_action
from django_filters.rest_framework import DjangoFilterBackend


class ActionDetailViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['polymorphic_ctype', "column", "date",
                        "recolte_nb", "created_time", "uptime"]

    @decorator_action(detail=False, methods=['get'], url_path='columns')
    def get_columns(self, request):
        queryset = Action.objects.order_by().values('column').distinct()
        serializer = ColumnSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorator_action(detail=False, methods=['get'], url_path='historic-breedings')
    def get_historic_breedings(self, request):
        queryset_mec = Action.objects.filter(polymorphic_ctype__in=[11, 14]).order_by('recolte_nb')
        serializer = HistoricBreedingsSerializer(queryset_mec, many=True)
        return Response(serializer.data)
