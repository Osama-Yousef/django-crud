from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Osama',
            email='osama@gmail.com',
            password='password'
        )

        self.post = Post.objects.create(
            title='apples',
            body='healthy food',
            author=self.user
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('blog_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_blog_update_view(self):
        response = self.client.post(reverse('blog_update', args='1'), {
            'title': 'chips',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')

    def test_home_status(self):
        expected = 200
        url = reverse('blogs')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_template(self):
        url = reverse('blogs')
        response = self.client.get(url)
        actual = 'blogs.html'
        self.assertTemplateUsed(response, actual)

    