#
#
#
#
#
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
#
from markdown import markdown
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to='blog_images/')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_slug(self):
        return slugify(self.title)

    def save(self, *args, **kwargs):
        self.processed_content = mark_safe(markdown(self.content))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.get_slug()})
