from django.test import TestCase
from rest_framework.test import APIClient
from .models import Company, Employee  # Import other models as needed


class CompanyAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company_data = {'name': 'Company A'}

    def test_create_company(self):
        response = self.client.post('/api/companies/', self.company_data, format='json')
        self.assertEqual(response.status_code, 201)
