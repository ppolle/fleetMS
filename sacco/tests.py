from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

# Create your tests here.
from fleet_base.models import User
from fleet_base.views import home

from .models import Sacco


class UserTestCase(TestCase):
    # Method that setsup the instance of the class
    def setUp(self):
        self.user = User.objects.create(
            username='test', email='test@test.com', password='test1234')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class SaccoViewTests(TestCase):
    # Test to make sure '/' url path returns home view
    def setUp(self):
        self.user = User.objects.create(
            username='test', email='test@test.com', password='test1234')
        self.sacco = Sacco.objects.create(name='test sacco', user='test', registration_no='12345678', office_location='test locale',
                                          office_telephone='0712345678', office_email='test@test.com', logo='tets.png', details='test details')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_sacco_details_page(self):
        sacco_url = reverse('sacco', kwargs={
            'pk': self.sacco.pk})
        self.assertContains(self.response, 'href="{0}"'.format(sacco_url))


class saccoTestClass(TestCase):
    def setUp(self):
        Sacco.objects.create(name='test sacco', user='test', registration_no='12345678', office_location='test locale',
                             office_telephone='0712345678', office_email='test@test.com', logo='tets.png', details='test details')

    def test_sacco_view_success_status_code(self):
        url = reverse('sacco', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_sacco_view_not_found_status_code(self):
        url = reverse('sacco', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_sacco_url_resolves_sacco_view(self):
        view = resolve('/saccos/1/')
        self.assertEquals(view.func, sacco)

    def test_sacco_view_contains_link_back_to_homepage(self):
        sacco_url = reverse('sacco', kwargs={'pk': 1})
        response = self.client.get(sacco_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NewsaccoTest(TestCase):
    def setUp(self):
        Sacco.objects.create(name='test sacco', user='test', registration_no='12345678', office_location='test locale',
                             office_telephone='0712345678', office_email='test@test.com', logo='tets.png', details='test details')

    def test_new_sacco_view_success_status_code(self):
        url = reverse('new_sacco', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_sacco_view_not_found_status_code(self):
        url = reverse('new_sacco', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_sacco_url_resolves_sacco_view(self):
        view = resolve('/saccos/1/new/')
        self.assertEquals(view.func, new_sacco)

    def test_sacco_view_contains_link_back_to_homepage(self):
        new_sacco_url = reverse('new_sacco', kwargs={'pk': 1})
        sacco_url = reverse('sacco', kwargs={'pk': 1})
        response = self.client.get(new_sacco_url)
        self.assertContains(response, 'href="{0}"'.format(sacco_url))
