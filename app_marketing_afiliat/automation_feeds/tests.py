#
#
#
#
#
from django.test import TestCase
from .models import Feeds, ContactForm
#
from django.urls import reverse
#
import requests
from .cron import scrape_and_insert
#
# big tests for pages
from bs4 import BeautifulSoup


class FeedsTestCase(TestCase):  # -------------> START: IMPORTANT TESTS <-------------

    def test_insert(self):
        # Test insert in DB
        Feeds.objects.create(
            title='Test Feed',
            affiliate_code='https://example.com',
            price=10.0,
            image_urls='image_url_1,image_url_2'
        )
        self.assertEqual(Feeds.objects.count(), 1)


class ScrapeAndInsertTest(TestCase):

    def test_scrape_and_insert(self):

        # Clean DB
        Feeds.objects.all().delete()

        response_text = requests.get(
            url='https://api.2performant.com/feed/ed1bc10cd.xml').text

        # requests.get - Simulation XML response
        class MockResponse:
            status_code = 200
            text = response_text

        # return simulation for requests.get
        original_requests_get = requests.get
        requests.get = lambda *args, **kwargs: MockResponse()

        # test my cron function for test
        scrape_and_insert()

        # Check if data inserted in DB correctly
        self.assertEqual(Feeds.objects.count(), 100)

        # re-request
        requests.get = original_requests_get


class ContactFormModelTest(TestCase):

    def test_create_contact_form(self):
        contact = ContactForm(
            nume='Andrei Cojocaru',
            email='andrei.reporter13@gmail.com',
            phone='0730449825',
            message='Test cu datele mele!'
        )

        # save date to db_default
        contact.save()

        # verify data ---> !
        saved_contact = ContactForm.objects.get(pk=contact.pk)
        self.assertEqual(saved_contact.nume, 'Andrei Cojocaru')
        self.assertEqual(saved_contact.email, 'andrei.reporter13@gmail.com')
        self.assertEqual(saved_contact.phone, '0730449825')
        self.assertEqual(saved_contact.message, 'Test cu datele mele!')

    def test_contact_form_str_method(self):
        contact = ContactForm(
            nume='Andrei Cojocaru',
            email='andrei.reporter13@gmail.com',
            phone='0730449825',
            message='Test pentru str -> nume!'
        )

        # Verify __str__ method
        self.assertEqual(str(contact), 'Andrei Cojocaru')  # -------------> END: IMPORTANT TESTS <-------------


class BsObject:  # -------------> START: TESTS FOR PAGES <-------------

    # get bs4 object from pages
    def find_element_by_tag(self, response, tag_name):
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(tag_name)
        return elements


class HomePageTest(BsObject, TestCase):

    def test_only_one_h1(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        h1 = self.find_element_by_tag(response, 'h1')
        self.assertTrue(len(h1) == 3)

    def test_image_if_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        img = self.find_element_by_tag(response, 'img')
        self.assertTrue(len(img) > 0)
