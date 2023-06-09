import json

from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase
from preferences.models import Preference

requests = APIClient()

payload_1 = {
    "id": 1,
    "version": 1,
    "value": 'set testing value',
    "path": '124d-wedfe-we49-ewwe33',
    "namespace": 'namespace-test-1',
    "user_id": 1,
}


class TestingPrefAdmin(TestCase):
    fixtures = ['resources/fixtures/default_data.json', ]

    def test_post_admin(self):
        requests.login(email='admin@goss.com', password='password')
        url = reverse('admin_preferences-list')
        data = requests.post(url, payload_1, format="json")

        self.assertEqual(data.status_code, 201)
        self.assertEqual(Preference.objects.count(), 6)
        requests.logout()

    def test_get_admin(self):
        requests.login(email='admin@goss.com', password='password')
        url = reverse('admin_preferences-list')
        data = requests.get(url)

        self.assertEqual(data.status_code, 200)
        requests.logout()

    def test_filter(self):
        requests.login(email='admin@goss.com', password='password')
        url = reverse('admin_preferences-list')
        filter_url = f'{url}?user=2'
        response = requests.get(filter_url)

        self.assertEqual(len(response.data['results']), 0)
        self.assertEqual(response.status_code, 200)

        requests.logout()

    def test_auth_admin_url(self):
        requests.login(email='user@goss.com', password='password')
        url = reverse('admin_preferences-list')
        filter_url = f'{url}?user=2'
        response = requests.get(filter_url, format="json")

        self.assertEqual(response.status_code, 403)
        requests.logout()
