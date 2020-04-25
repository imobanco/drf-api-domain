from rest_framework import serializers


class ServiceSeralizer(serializers.ModelSerializer):
    """
    Sobreescrevemos os métodos create, update e save para garantir que a camada 'view'
    não tenho acesso direto à escrita da camada 'model'.
    """

    def create(self, validated_data):
        raise NotImplementedError("Não use o método 'create' do serializer!")

    def update(self, instance, validated_data):
        raise NotImplementedError("Não use o método 'update' do serializer!")

    def save(self, **kwargs):
        raise NotImplementedError("Não use o método 'save' do serializer!")
