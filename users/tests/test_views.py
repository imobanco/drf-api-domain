from rest_framework import status

from core.test_utils import BaseAPIJWTTestCase, ImageTestCaseMixin
from users.factories import UserFactory, User


class UsersAPITestCase(BaseAPIJWTTestCase, ImageTestCaseMixin):
    def setUp(self):
        super().setUp()
        self.endpoint = "users"

    # CREATE
    def test_post(self):
        self.assertEqual(User.objects.count(), 0)

        data = {
            "email": "test@gmail.com",
            "password": "test123"
        }

        path = self.get_path()

        response = self.client.post(path, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, msg=response.data
        )

        self.assertEqual(User.objects.count(), 1)

        user = User.objects.first()
        self.assertEqual(user.email, "test@gmail.com")
        self.assertTrue(user.has_usable_password())

    # PUT
    def test_put(self):
        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)
        self.set_user(user)

        self.assertEqual(user.email, "foo@bar.com")

        data = {
            "password": user.password,
            "email": "bar@foo.com",
        }

        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)

        user.refresh_from_db()
        self.assertEqual(user.email, "bar@foo.com")

    def test_put_other_user(self):
        my_user = UserFactory()
        self.set_user(my_user)

        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)

        self.assertEqual(user.email, "foo@bar.com")

        data = {"password": user.password, "email": user.email}

        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data
        )
        self.assertEqual(User.objects.count(), 2)

        user.refresh_from_db()
        self.assertEqual(user.email, "foo@bar.com")

    def test_put_fail_missing_fields(self):
        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)
        self.set_user(user)

        self.assertEqual(user.email, "foo@bar.com")

        data = {}

        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data
        )
        self.assertEqual(User.objects.count(), 1)

        user.refresh_from_db()
        self.assertEqual(user.email, "foo@bar.com")

    # PATCH
    def test_patch(self):
        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)
        self.set_user(user)

        self.assertEqual(user.email, "foo@bar.com")

        data = {"email": "bar@foo.com"}

        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)

        user.refresh_from_db()
        self.assertEqual(user.email, "bar@foo.com")

    def test_patch_picture(self):
        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)
        self.set_user(user)

        self.assertEqual(user.email, "foo@bar.com")

        data = {"picture": open(self._image_path, "rb")}

        path = self.get_path(id_detail=user.id)

        response = self.client.patch(
            path, data, HTTP_AUTHORIZATION=self.auth, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)

        user.refresh_from_db()
        self.assertEqual(user.picture.name, f"users/{user.id}/picture.jpg")

    def test_patch_fail(self):
        user = UserFactory(email="foo@bar.com")
        self.assertIsInstance(user, User)
        self.set_user(user)

        self.assertEqual(user.email, "foo@bar.com")

        data = {"email": ""}

        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data
        )
        self.assertEqual(User.objects.count(), 1)

        user.refresh_from_db()
        self.assertEqual(user.email, "foo@bar.com")

    # LIST
    def test_list_unauthorized(self):
        UserFactory.create_batch(3)
        self.assertEqual(User.objects.count(), 3)

        path = self.get_path()

        response = self.client.get(path)
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data
        )

    def test_list(self):
        users = UserFactory.create_batch(3)
        self.assertEqual(User.objects.count(), 3)
        self.set_user(users[0])

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get("results")), 1, msg=response.data)

    # RETRIEVE
    def test_get(self):
        user = UserFactory(email="foo@bar.com")
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        path = self.get_path(id_detail=user.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get("email"), "foo@bar.com")

    # DELETE
    def test_delete(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        self.set_user(user)

        path = self.get_path(id_detail=user.id)

        response = self.client.delete(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)

        self.assertEqual(User.objects.count(), 0)