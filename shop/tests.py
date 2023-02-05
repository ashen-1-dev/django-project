from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class HomePageViewTest(TestCase):
  def test_view_url_exists_at_proper_location(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
  def test_view_url_by_name(self):
    response = self.client.get(reverse('shop:homepage'))
    self.assertEqual(response.status_code, 200)
  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('shop:homepage'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'shop/home.html')