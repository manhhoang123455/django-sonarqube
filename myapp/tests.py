# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# import os

# mypassword = os.getenv("TEST_USER_PASSWORD", "TEST_USER_PASSWORD")
# mypassword_wrong = os.getenv("TEST_USER_PASSWORD_WRONG", "TEST_USER_PASSWORD_WRONG")


# class LoginTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password=mypassword)
#         self.login_url = reverse("login")

#     def test_login_success(self):
#         response = self.client.post(
#             self.login_url, {"username": "testuser", "password": mypassword}
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("access", response.data)
#         self.assertIn("refresh", response.data)

#     def test_login_failure(self):
#         response = self.client.post(
#             self.login_url, {"username": "wronguser", "password": mypassword_wrong}
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertNotIn("access", response.data)
#         self.assertNotIn("refresh", response.data)
