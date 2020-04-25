def picture_path(instance, filename, *args, **kwargs):
    return f'users/{instance.id}/picture.{filename.split(".")[-1]}'
