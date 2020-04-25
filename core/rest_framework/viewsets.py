from rest_framework.viewsets import GenericViewSet

from .mixins import (
    CreateServiceMixin,
    DestroyServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
)


class ServiceGenericViewSet(GenericViewSet):
    """
    GenericViewSet que utiliza a camada service e não o model diretamente.

    O :attr:`.service` substitui o :attr:`.queryset`.
    """
    nested_serializer_class = None
    service = None

    def get_serializer_class(self):
        """
        Utilitário para retornar serializers nested (com outros serializers em relação de objetos).

        Returns:
            :attr:`.nested_serializer_class` ou :attr:`.serializer_class`
        """
        try:
            if self.nested_serializer_class and self.request.query_params.get("nested"):
                return self.nested_serializer_class
        except AttributeError:
            pass
        return self.serializer_class

    def get_queryset(self):
        """
        Sobreescrevemos esse método para utilizar o atributo :attr:`.service`
        ao invés do :attr:`.queryset`.

        Returns:
            :class:`.QuerySet`
        """
        if self.action == 'list':
            """pode ser que o usuário queira restringir os objetos retornados na listagem"""
            return self.service.list_for_request(self.request)
        return self.service.list()


class ServiceViewSet(
    CreateServiceMixin,
    DestroyServiceMixin,
    ListServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
    ServiceGenericViewSet,
):
    pass
