#
#
#
#
#
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        Post.objects.create(
            title='Affiliate Marketing',
            content='Affiliate Marketing test content. Awesome.',
            author=user,
            slug='affiliate-marketing',
            published_date=None
        )

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.slug, 'affiliate-marketing')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/affiliate-marketing/')
