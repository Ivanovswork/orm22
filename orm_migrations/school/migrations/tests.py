from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_view_200(self):
        url = 'http://194.58.103.43/students/'
        client = APIClient()
        response = client.get(url)
        self.assertEquals(200, 200)
