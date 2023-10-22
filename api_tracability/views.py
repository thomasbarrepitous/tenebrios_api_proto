from django.utils.formats import date_format
from polymorphic.base import PolymorphicQuerySet
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from api_tracability.serializers import (
    ActionSerializer,
    ColumnSerializer,
    ActionPolymorphicSerializer,
    HistoricBreedingsSerializer,
    HarvestSerializer,
)
from api_tracability.models import Action
from rest_framework.decorators import action as decorator_action
from django_filters.rest_framework import DjangoFilterBackend
from functools import wraps
from django.db.models import QuerySet
from datetime import datetime


def paginateHarvest(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        queryset = func(self, *args, **kwargs)
        assert isinstance(
            queryset, (list, QuerySet)
        ), "apply_pagination expects a List or a QuerySet"
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = HarvestSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = HarvestSerializer(queryset, many=True)
        return Response(serializer.data)

    return inner


class ActionDetailViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "polymorphic_ctype",
        "column",
        "date",
        "recolte_nb",
        "created_time",
        "uptime",
    ]

    def generate_recolte_nb(self, column, date):
        latest_action = Action.objects.filter(column=column).order_by("-date").first()
        if latest_action is None:
            return column + date_format(datetime.fromisoformat(date), "md")
        latest_date = latest_action.date
        latest_actions = Action.objects.filter(column=column, date=latest_date)
        # We need to proceed this way as a recolte can be the same day as anther action.
        recolte_in_latest_actions = latest_actions.filter(polymorphic_ctype=14)
        # IF in the latest actions, there is a 'recolte' action we generate a new recolte-nb a new one.
        print(recolte_in_latest_actions == Action.objects.none())

        if recolte_in_latest_actions:
            date = datetime.fromisoformat(date)
            return column + date_format(date, "md")
        return latest_action.recolte_nb

    def create(self, request, *args, **kwargs):
        # If lastest action is a 'recolte' we create a new one.
        recolte_nb = self.generate_recolte_nb(
            request.data.get("column"), request.data.get("date")
        )
        input_data = request.data.dict() | {"recolte_nb": recolte_nb}
        serializer = self.get_serializer(data=input_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @decorator_action(detail=False, methods=["get"], url_path="columns")
    def get_columns(self, request):
        queryset = Action.objects.order_by().values("column").distinct()
        serializer = ColumnSerializer(queryset, many=True)
        return Response(serializer.data)

    @paginateHarvest
    @decorator_action(detail=False, methods=["get"], url_path="recolte-nb")
    def get_harvest(self, request):
        column = request.query_params.getlist("column")
        queryset = Action.objects.order_by().values("recolte_nb").distinct()
        if column:
            queryset = (
                Action.objects.filter(column__in=column)
                .order_by()
                .values("recolte_nb")
                .distinct()
            )
        return queryset

    @decorator_action(detail=False, methods=["get"], url_path="historic-breedings")
    def get_historic_breedings(self, request):
        # Handle multiple column filtering
        column = request.query_params.getlist("column")
        queryset = Action.objects.filter(polymorphic_ctype__in=[11, 14]).order_by(
            "recolte_nb"
        )
        if column:
            queryset = Action.objects.filter(
                polymorphic_ctype__in=[11, 14], column__in=column
            ).order_by("recolte_nb")
        serializer = HistoricBreedingsSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorator_action(
        detail=False, methods=["get"], url_path=r"recolte-nb/(?P<recolte_nb>[^/.]+)"
    )
    def get_recolte_info(self, request, recolte_nb=None):
        try:
            queryset = Action.objects.filter(recolte_nb=recolte_nb)
        except Action.DoesNotExist:
            return Response(
                {"error": "Recolte_nb not found."}, status=status.HTTP_400_BAD_REQUEST
            )
        # serializer = HistoricBreedingsSerializer(queryset, many=True)
        serializer = ActionPolymorphicSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorator_action(
        detail=False,
        methods=["get"],
        url_path=r"recolte-nb/(?P<recolte_nb>[^/.]+)/cycle",
    )
    def get_breeding_cycle(self, request, recolte_nb=None):
        try:
            queryset_cycle = Action.objects.filter(
                recolte_nb=recolte_nb, polymorphic_ctype__in=[11, 14]
            )
        except Action.DoesNotExist:
            return Response(
                {"error": "Cycle not found."}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = HistoricBreedingsSerializer(queryset_cycle, many=True)
        return Response(serializer.data)
