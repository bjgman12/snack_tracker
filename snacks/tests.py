from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SnackTests(TestCase):
    def test_snack_list(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
    def test_list_extends(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_template(self):
        url = reverse('snack_list')
        response = self.client.get(url + '/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_extends(self):
        url = reverse('snack_list')
        response = self.client.get(url + '/1/')
        self.assertTemplateUsed(response, 'base.html')