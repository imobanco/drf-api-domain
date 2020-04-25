from core.rest_framework.permissions import IsAuthenticatedOrCreate, IsOwnerOrAdmin
from core.rest_framework.viewsets import ServiceViewSet

from .serializers import UserSerializer
from ..services import UserService


class UserViewSet(ServiceViewSet):
    """
    API resource com todos os verbatins HTTP
    """

    service = UserService
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwnerOrAdmin]
    filter_fields = []
