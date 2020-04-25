from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class CreateServiceMixin(CreateModelMixin):
    """
    Sobreescrevemos o create para chamar o método create do Service, e não do serializer.
    """

    def create(self, request, *args, **kwargs):
        """
        Verbo http create
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.service.create(**serializer.validated_data)
        serializer = self.get_serializer(instance)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class DestroyServiceMixin(DestroyModelMixin):
    """
    Sobreescrevemos o destroy para chamar o método delete do Service, e não do object.
    """

    def destroy(self, request, *args, **kwargs):
        """
        Verbo HTTP delete
        """
        instance = self.get_object()

        self.service.delete(instance.id)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListServiceMixin(ListModelMixin):
    """
    Não precisamos sobreescrever a ação list.

    É apenas de leitura.
    """

    def list(self, request, *args, **kwargs):
        """
        Verbo HTTP list
        """
        return super().list(request, *args, **kwargs)


class RetrieveServiceMixin(RetrieveModelMixin):
    """
    Não precisamos sobreescrever a ação retrieve.

    É apenas de leitura.
    """

    def retrieve(self, request, *args, **kwargs):
        """
        Verbo HTTP retrieve
        """
        return super().retrieve(request, *args, **kwargs)


class UpdateServiceMixin(UpdateModelMixin):
    """
    Sobreescrevemos o update para chamar o método update do Serice, e não do serializer.

    Não precisamos sobreescrever o partial_update, ele chama o update.
    """

    def update(self, request, *args, **kwargs):
        """
        Verbo HTTP put
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        instance = self.service.update(instance.id, **serializer.validated_data)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Verbo HTTP patch
        """
        return super().partial_update(request, *args, **kwargs)
