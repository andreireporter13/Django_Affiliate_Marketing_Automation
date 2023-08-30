#
#
#
#
#
#
import xml.etree.ElementTree as ET
import requests
from .models import Feeds


def scrape_and_insert():
    '''
    ... this funct will scrape data from 2performant site,
    ... and store all data into a database, use Django Model.
    '''

    # VERY IMPORTANT ---> Clean DataBase
    Feeds.objects.all().delete()

    response = requests.get(
        url='https://api.2performant.com/feed/ed1bc10cd.xml')
    if response.status_code == 200:
        xml_text = response.text
        root = ET.fromstring(xml_text)

        for idx, item in enumerate(root.findall('item')):
            if idx >= 100:  # no more 100 products
                break

            # parse products
            title = item.find('title').text
            aff_code = item.find('aff_code').text
            price = float(item.find('price').text)  # Convert to float
            image_urls = item.find('image_urls').text

            # Insert data into the database
            Feeds.objects.create(
                title=title,
                affiliate_code=aff_code,
                price=price,
                image_urls=image_urls
            )

    else:
        print("Error downloading XML content")
