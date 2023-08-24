#
#
#
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'automation_feeds/home.html'


class PromotionsPageView(TemplateView):
    template_name = 'automation_feeds/promotions.html'


class FeedsPageView(TemplateView):
    template_name = 'automation_feeds/feeds.html'


class ShopsPageView(TemplateView):
    template_name = 'automation_feeds/shops.html'


class ContactPageView(TemplateView):
    template_name = 'automation_feeds/contact.html'
