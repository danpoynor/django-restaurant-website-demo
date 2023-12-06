from django.test import TestCase
from django.urls import reverse
from .models import Menu
from .forms import BookingForm


class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Test dish", price=10,
                            description="Test description")

    def test_menu_content(self):
        dish = Menu.objects.get(id=1)
        expected_object_name = f'{dish.name}'
        self.assertEqual(expected_object_name, 'Test dish')


class HomePageViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Test dish", price=10,
                            description="Test description")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


# Test Suites for Views
class MenuPageViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Test dish", price=10,
                            description="Test description")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/menu/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('menu'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('menu'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu.html')


class AboutPageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about.html')


class BookPageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/book/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('book'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('book'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'book.html')


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            name="Test dish", price=10, description="Test description")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get(f'/menu_item/{self.menu_item.pk}/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('menu_item', args=[self.menu_item.pk]))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('menu_item', args=[self.menu_item.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu_item.html')

    def test_view_has_correct_context_data(self):
        resp = self.client.get(reverse('menu_item', args=[self.menu_item.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['menu_item'], self.menu_item)

    def test_page_not_found_for_menu_item_that_does_not_exist(self):
        resp = self.client.get('/menu/99999/')
        self.assertEqual(resp.status_code, 404)


# Test Suites for Models
class BookingFormTest(TestCase):
    def test_form_valid(self):
        form = BookingForm(data={
                           'first_name': 'Test First Name', 'last_name': 'Test Last Name', 'guest_number': '99', 'comment': 'Test Comment'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())

    def test_form_first_name_field_error(self):
        form = BookingForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], [
                         'This field is required.'])
