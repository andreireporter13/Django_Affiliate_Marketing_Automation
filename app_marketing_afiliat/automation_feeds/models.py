#
#
#
#
#
#
from django.db import models


class Feeds(models.Model):
    title = models.CharField(max_length=255)
    affiliate_code = models.URLField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_urls = models.TextField()

    def __str__(self):
        return self.title
