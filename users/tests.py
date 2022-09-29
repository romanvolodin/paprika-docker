from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        email = "test@email.com"
        password = "Passwd123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@EMAIL.com"
        user = get_user_model().objects.create_user(email, "Passwd123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Passwd123")

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser("test@email.com", "Passwd123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "admin@email.com", "Admin1234"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@email.com",
            password="User1234",
            first_name="Testname",
            last_name="Testlastname",
        )

    def test_users_listed(self):
        url = reverse("admin:users_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_user_change_page(self):
        url = reverse("admin:users_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        url = reverse("admin:users_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
