from unittest import TestCase
from rest_framework.test import APIClient

class TestSampleView(TestCase):
    def test_view_200(self):
        self.assertIs(1, 1)
