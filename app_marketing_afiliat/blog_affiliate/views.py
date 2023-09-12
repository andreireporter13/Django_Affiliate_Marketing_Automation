#
#
#
#
#
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import Http404


class BlogPageView(ListView):
    model = Post
    template_name = 'blog_affiliate/blog.html'
    context_object_name = 'page'
    ordering = ['-created_date']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_affiliate/post_detail.html'
    context_object_name = 'post'
    slug_field = 'post_slug'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get('post_slug')

        try:
            post = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            raise Http404("Acest blog post nu exista!")

        return post
