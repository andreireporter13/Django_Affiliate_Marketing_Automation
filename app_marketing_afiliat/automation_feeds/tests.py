#
#
#
#
#
from django.test import TestCase
from .models import Feeds, ContactForm
#
import requests
from .cron import scrape_and_insert
#


class FeedsTestCase(TestCase):

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
        self.assertEqual(str(contact), 'Andrei Cojocaru')
