#
#
#
#
#
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Category


class BlogPageView(ListView):
    model = Post
    template_name = 'blog_affiliate/blog.html'
    context_object_name = 'page'
    ordering = ['-created_date']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_affiliate/post_detail.html'
    context_object_name = 'post'
    slug_field = 'post_slug'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')

        category = get_object_or_404(Category, slug=category_slug)
        post = get_object_or_404(Post, slug=post_slug, category=category)

        return post
