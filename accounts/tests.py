from django.test import TestCase

from accounts.factories import UserFactory, StaffUserFactory, AdminUserFactory


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.staff_user = StaffUserFactory()
        self.admin_user = AdminUserFactory()

    def test_authenticate_user(self):
        data = {
            "email": self.user.email,
            "password": self.user.password,
        }
        response = self.client.post("/accounts/authenticate/", data)
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        self.client.force_login(user=self.user)
        response = self.client.get("/accounts/logout")
        self.assertEqual(response.url, "/accounts/logout/")
        self.assertEqual(response.status_code, 301)
