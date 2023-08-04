from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_view_200(self):
        url = '/students/'
        client = APIClient()
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
