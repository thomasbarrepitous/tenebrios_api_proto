from rest_framework import viewsets
from rest_framework import permissions
from api_tracability.serializers import ActionSerializer
from api_tracability.models import Action


class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [permissions.IsAuthenticated]