class ModelService:
    MODEL = None

    @classmethod
    def create(cls, **kwargs):
        return cls.MODEL.objects.create(**kwargs)

    @classmethod
    def update(cls, id, **kwargs):
        instance = cls.retrieve(id)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def retrieve(cls, id):
        return cls.MODEL.objects.get(id=id)

    @classmethod
    def list(cls):
        return cls.MODEL.objects.all()

    @classmethod
    def list_for_request(cls, request):
        return cls.list()

    @classmethod
    def get(cls, **kwargs):
        return cls.MODEL.objects.get(**kwargs)

    @classmethod
    def filter(cls, *args, **kwargs):
        return cls.MODEL.objects.filter(*args, **kwargs)

    @classmethod
    def last(cls, *args, **kwargs):
        return cls.filter(*args, **kwargs).last()
