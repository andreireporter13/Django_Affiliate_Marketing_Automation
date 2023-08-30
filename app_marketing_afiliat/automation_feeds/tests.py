#
#
#
#
#
from django.test import TestCase
from .models import Feeds
#
import requests
from .cron import scrape_and_insert


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
