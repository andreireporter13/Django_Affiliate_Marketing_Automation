#
#
#
#
#
#
#
from django.views.generic import TemplateView, ListView
from .models import Feeds


# process feeds here
def process_feeds(feeds):
    for product in feeds:
        if '-' in product.title:
            product.split_title = product.title.split('-')[0]
        else:
            product.split_title = product.title


class HomePageView(TemplateView):
    template_name = 'automation_feeds/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feeds = Feeds.objects.all()[:8]
        process_feeds(feeds)
        context['feeds'] = feeds
        return context


class PromotionsPageView(TemplateView):
    template_name = 'automation_feeds/promotions.html'


class FeedsPageView(ListView):
    model = Feeds
    template_name = 'automation_feeds/feeds.html'
    context_object_name = 'page'
    paginate_by = 12


class ShopsPageView(TemplateView):
    template_name = 'automation_feeds/shops.html'


class ContactPageView(TemplateView):
    template_name = 'automation_feeds/contact.html'
