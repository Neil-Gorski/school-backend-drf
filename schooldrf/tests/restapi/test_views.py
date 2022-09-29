import pytest 
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse



class TestExamsAPIView(APITestCase):
    @pytest.mark.django_db
    def test_get_exams(self):
        url = reverse("api:exams-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEquals(response.status_code, HTTP_200_OK)
        