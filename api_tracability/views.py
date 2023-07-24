from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api_tracability.serializers import ColumnSerializer, ActionPolymorphicSerializer
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

    @decorator_action(detail=False, methods=['get'])
    def get_columns(self, request):
        queryset = Action.objects.order_by().values('column').distinct()
        serializer = ColumnSerializer(queryset, many=True)
        return Response(serializer.data)
