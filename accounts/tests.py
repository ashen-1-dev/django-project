import time

from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import CustomUser



# class UserTestCase(TestCase):
#   def setUp(self):
#     self.test_user = CustomUser.objects.create(
#       passport='12345t',
#       username='test_user',
#       email='test_user@gmail.com',
#       first_name='test_first',
#       last_name='test_last',
#       type='staff')
#
#   def test_user_created(self):
#     self.assertEqual(self.test_user.passport, '12345t')
#     self.assertEqual(self.test_user.username, 'test_user')
#     self.assertEqual(self.test_user.email, 'test_user@gmail.com')
#     self.assertEqual(self.test_user.first_name, 'test_first')
#     self.assertEqual(self.test_user.last_name, 'test_last')
#     self.assertEqual(self.test_user.type, 'staff')
#     self.assertNotEqual(self.test_user.type, 'patient')
#
#
# class CustomerListTestCase(LiveServerTestCase):
#   def setUp(self):
#     self.client.login(username="alant", password="alan123")
#     self.selenium = webdriver.Chrome()
#     self.selenium.maximize_window()
#     self.selenium.get('http://127.0.0.1:8000/')
#     super(CustomerListTestCase, self).setUp()
#
#   def tearDown(self):
#     self.selenium.quit()
#     super(CustomerListTestCase, self).tearDown()
#
#   def test_succesful_login(self, username="donk", password="don123", next_url=None):
#     self.selenium.get('http://127.0.0.1:8000/users/login/')
#     username_el = self.selenium.find_element("id_username")
#     username_el.send_keys(username)
#     password_el = self.selenium.find_element("id_password")
#     password_el.send_keys(password)
#     submit = self.selenium.find_element('loginButton')
#     submit.send_keys(Keys.RETURN)
#     time.sleep(3)
#     print(self.selenium.page_source)
#     assert 'Здравствуйте, Donald Knut.' in self.selenium.page_source
#
#   def test_unsuccesful_login(self, username="alant", password="alan1234", next_url=None):
#     self.selenium.get('http://127.0.0.1:8000/users/login/')
#     username_el = self.selenium.find_element("id_username")
#     username_el.send_keys(username)
#     password_el = self.selenium.find_element("id_password")
#     password_el.send_keys(password)
#     submit = self.selenium.find_element('loginButton')
#     submit.send_keys(Keys.RETURN)
#     time.sleep(3)
#     assert 'Please enter a correct username and password.' in self.selenium.page_source