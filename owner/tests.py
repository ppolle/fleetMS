from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

# Create your tests here.


class OwnerTestCase(TestCase):
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

    def test_home_view_contains_link_to_sacco_details_page(self):
        user_url = reverse('home', kwargs={
            'pk': self.id})
        self.assertContains(self.response, 'href="{0}"'.format(user_url))
