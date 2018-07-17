from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

# Create your tests here.
from .models import Supervisor
from .views import home, new_supervisor, supervisor

# Create your tests here.


class SupervisorViewTests(TestCase):
    # Test to make sure '/' url path returns home view
    def setUp(self):
        self.supervisor = Supervisor.objects.create(first_name='alvin', last_name='chipmink', id_number='12345678', date_of_birth='1989-09-12',
                                                    mobile_phone_number='0712345678', email='test@test.com', profile_picture='tets.png', sacco_base='test sacco')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_supervisor_details_page(self):
        supervisor_url = reverse('supervisor', kwargs={
                                 'pk': self.supervisor.pk})
        self.assertContains(self.response, 'href="{0}"'.format(supervisor_url))


class SupervisorTestClass(TestCase):
    def setUp(self):
        Supervisor.objects.create(first_name='alvin', last_name='chipmink', id_number='12345678', date_of_birth='12/09/1989',
                                  mobile_phone_number='0712345678', email='test@test.com', profile_picture='tets.png', details='test description')

    def test_supervisor_view_success_status_code(self):
        url = reverse('supervisor', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_supervisor_view_not_found_status_code(self):
        url = reverse('supervisor', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_supervisor_url_resolves_supervisor_view(self):
        view = resolve('/supervisors/1/')
        self.assertEquals(view.func, supervisor)

    def test_supervisor_view_contains_link_back_to_homepage(self):
        supervisor_url = reverse('supervisor', kwargs={'pk': 1})
        response = self.client.get(supervisor_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NewsupervisorTest(TestCase):
    def setUp(self):
        supervisor.objects.create(first_name='alvin', last_name='chipmink', id_number='12345678', date_of_birth='12/09/1989',
                                  mobile_phone_number='0712345678', email='test@test.com', profile_picture='tets.png', details='test description')

    def test_new_supervisor_view_success_status_code(self):
        url = reverse('new_supervisor', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_supervisor_view_not_found_status_code(self):
        url = reverse('new_supervisor', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_supervisor_url_resolves_supervisor_view(self):
        view = resolve('/supervisors/1/new/')
        self.assertEquals(view.func, new_supervisor)

    def test_supervisor_view_contains_link_back_to_homepage(self):
        new_supervisor_url = reverse('new_supervisor', kwargs={'pk': 1})
        supervisor_url = reverse('supervisor', kwargs={'pk': 1})
        response = self.client.get(new_supervisor_url)
        self.assertContains(response, 'href="{0}"'.format(supervisor_url))
