from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api_tracability.serializers import ActionSerializer, ColumnSerializer, ActionDetailPolymorphicSerializer
from api_tracability.models import ActionDetail, Action as TracabilityAction
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


class ActionDetailViewSet(viewsets.ModelViewSet):
    queryset = ActionDetail.objects.all()
    serializer_class = ActionDetailPolymorphicSerializer


class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TracabilityAction.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["action_detail", "column",
                        "recolte_nb", "created_time", "uptime"]

    @action(detail=False, methods=['get'])
    def get_columns(self, request):
        queryset = TracabilityAction.objects.order_by().values('column').distinct()
        serializer = ColumnSerializer(queryset, many=True)
        return Response(serializer.data)
