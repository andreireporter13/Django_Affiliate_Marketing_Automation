#
#
#
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = 'automation_feeds/home.html'


def promotions(request):
    return HttpResponse('<h1>Promotions</h1>')


def feeds(request):
    return HttpResponse('<h1>Feeds</h1>')


def shops(request):
    return HttpResponse('<h1>Shops</h1>')
