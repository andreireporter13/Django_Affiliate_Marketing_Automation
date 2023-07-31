#
#
#
from django.views.generic import TemplateView
from django.shortcuts import render


class BlogPageView(TemplateView):
    template_name = 'blog_affiliate/blog.html'
