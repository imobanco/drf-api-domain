import os
import requests
import shutil

from django.conf import settings
from django.test import TestCase
from django.test.runner import DiscoverRunner
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class ImageTestCaseMixin(TestCase):
    def setUp(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        root_path = os.path.join(current_path, os.pardir)
        self._media_path = os.path.join(root_path, "media")
        try:
            os.mkdir(self._media_path)
        except FileExistsError:
            pass
        self.image_name = "local_image.jpg"

        self._image_path = os.path.join(self._media_path, self.image_name)

        self._create_image()

    @staticmethod
    def get_image_raw():
        lorem_picsum_url = "https://picsum.photos/200/300"
        resp = requests.get(lorem_picsum_url, stream=True)
        resp.raw.decode_content = True
        return resp.raw

    def _create_image(self):
        image_raw = self.get_image_raw()

        local_file = open(self._image_path, "wb")
        shutil.copyfileobj(image_raw, local_file)
        local_file.close()
        return local_file


class BaseAPITestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = None

    def get_path(self, id_detail=None, action=None, _filter=None):
        if not self.endpoint:
            raise AttributeError("Endpoint não definido")
        path = f"/{self.endpoint}/"
        if id_detail:
            path += f"{id_detail}/"
        if action:
            path += f"{action}/"
        if _filter:
            path += f"?{_filter}"
        return path


class BaseAPIJWTTestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.user = None
        self.token = None

    @property
    def auth(self):
        if not self.token:
            raise ValueError(
                "Chame o método set_user passando o " "usuário antes de utilizar o auth"
            )
        return f"Bearer {self.token.access_token}"

    def set_user(self, user):
        self.user = user
        self.token = RefreshToken.for_user(self.user)


class MyTestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.TEST = True
        super(MyTestSuiteRunner, self).__init__(*args, **kwargs)
