from ..services import UserService
from ..models import User
from ..factories import UserFactory
from core.test_utils import ImageTestCaseMixin


class UserServiceTestCase(ImageTestCaseMixin):
    def test_create(self):
        user = UserService.create(
            email="foo@bar.com", password="senha", picture=self.image_name
        )

        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "foo@bar.com")
        self.assertTrue(user.has_usable_password())
        self.assertEqual(user.picture.name, self.image_name)
        self.assertTrue(user._picture.url)

    def test_update_password(self):
        user = UserFactory()

        self.assertIsInstance(user, User)
        self.assertFalse(user.has_usable_password())

        user = UserService.update(user.id, password="nova senha")

        self.assertTrue(user.has_usable_password())

    def test_update_picture(self):
        user = UserService.create(email="foo@bar.com")

        self.assertIsInstance(user, User)

        user = UserService.update(user.id, picture=self.image_name)

        self.assertEqual(user.picture.name, self.image_name)
        self.assertTrue(user._picture.url)
