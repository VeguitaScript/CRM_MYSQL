from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class SecurityTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.protected_url = reverse('ruta_protegida')

        # Crea un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.token, created = Token.objects.get_or_create(user=self.user)

    def test_protected_route_requires_authentication(self):
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_route_with_valid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()