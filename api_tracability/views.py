from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from api_tracability.serializers import ColumnSerializer, ActionPolymorphicSerializer, HistoricBreedingsSerializer, HarvestSerializer
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

    @decorator_action(detail=False, methods=['get'], url_path='recolte-nb')
    def get_harvest(self, request):
        queryset = Action.objects.order_by().values('recolte_nb').distinct()
        serializer = HarvestSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorator_action(detail=False, methods=['get'], url_path='historic-breedings')
    def get_historic_breedings(self, request):
        queryset_mec = Action.objects.filter(
            polymorphic_ctype__in=[11, 14]).order_by('recolte_nb')
        serializer = HistoricBreedingsSerializer(queryset_mec, many=True)
        return Response(serializer.data)

    @decorator_action(detail=False, methods=['get'], url_path=r'recolte-nb/(?P<recolte_nb>[^/.]+)')
    def get_recolte_info(self, request, recolte_nb=None):
        try:
            queryset = Action.objects.filter(
                recolte_nb=recolte_nb)
        except Action.DoesNotExist:
            return Response({"error": "Recolte_nb not found."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = HistoricBreedingsSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorator_action(detail=False, methods=['get'], url_path=r'recolte-nb/(?P<recolte_nb>[^/.]+)/cycle')
    def get_breeding_cycle(self, request, recolte_nb=None):
        try:
            queryset_cycle = Action.objects.filter(
                recolte_nb=recolte_nb, polymorphic_ctype__in=[11, 14])
        except Action.DoesNotExist:
            return Response({"error": "Cycle not found."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = HistoricBreedingsSerializer(queryset_cycle, many=True)
        return Response(serializer.data)
