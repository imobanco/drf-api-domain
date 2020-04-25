from core.rest_framework.permissions import IsAuthenticated, IsOwnerOrAdmin
from core.rest_framework.viewsets import ServiceViewSet

from .serializers import UserSerializer
from ..services import UserService


class UserViewSet(ServiceViewSet):
    """
    API resource com todos os verbatins HTTP
    """

    service = UserService
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_fields = []
