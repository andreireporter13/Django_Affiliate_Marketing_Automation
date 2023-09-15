#
#
#
#
#
from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404
from .models import Post


class BlogPageView(ListView):
    model = Post
    template_name = 'blog_affiliate/blog.html'
    context_object_name = 'page'
    ordering = ['-created_date']
    paginate_by = 2


class PostDetailView(TemplateView):
    template_name = 'blog_affiliate/blog_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        context['post'] = post
        return context
