from ..services import UserService
from ..models import User
from core.test_utils import ImageTestCaseMixin


class UserServiceTestCase(ImageTestCaseMixin):
    def test_create(self):
        user = UserService.create(email="foo@bar.com", picture=self.image_name)

        self.assertIsInstance(user, User)
        self.assertEqual(user.picture.name, self.image_name)
        self.assertTrue(user._picture.url)

    def test_update(self):
        user = UserService.create(email="foo@bar.com")

        self.assertIsInstance(user, User)

        user = UserService.update(user.id, picture=self.image_name)

        self.assertEqual(user.picture.name, self.image_name)
        self.assertTrue(user._picture.url)
