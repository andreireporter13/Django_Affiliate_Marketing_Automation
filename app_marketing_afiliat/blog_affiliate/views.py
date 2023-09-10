#
#
#
#
#
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post, Category
from django.http import Http404


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

        try:
            category = Category.objects.get(slug=category_slug)
            post = Post.objects.get(slug=post_slug, category=category)
        except Category.DoesNotExist:
            # Dacă categoria nu există, poți să setezi o categorie implicită sau să arunci o excepție Http404.
            # Iată un exemplu cu o categorie implicită cu numele 'General':
            category = Category.objects.get_or_create(name='General')[0]
            post = Post.objects.get(slug=post_slug, category=category)
            raise Http404("Categoria specificată nu există")

        return post
