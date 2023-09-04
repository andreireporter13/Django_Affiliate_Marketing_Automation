#
#
#
#
#
#
#
from django.views.generic import TemplateView, ListView
from .models import Feeds
from .forms import ContactFormData
from django.shortcuts import render, redirect


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

    def get(self, request, *args, **kwargs):
        context = {'form': ContactFormData()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactFormData(request.POST)
        if form.is_valid():
            # save to db
            form.save()
            # redirect to succes page
            return redirect('succes-contact')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class SuccesContactForm(TemplateView):
    template_name = 'automation_feeds/succes_contact.html'
