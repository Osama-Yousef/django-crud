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

    
    def test_string_representation(self):
        post = Post(title='title')
        self.assertEqual(str(post), post.title)

    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'apples')
        self.assertEqual(f'{self.post.author}', 'Osama')
        self.assertEqual(self.post.body, 'healthy food')

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
    
    def test_create_view(self):
        response = self.client.post(reverse('blog_create'), {
            'title': 'chips',
            'author': self.user,
            'body' :'healthy food',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')
        self.assertContains(response, 'healthy food')
        self.assertContains(response, 'Osama')

    def test_delete_view(self):
        response = self.client.get(reverse('blog_delete', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete?')

        post_response = self.client.post(reverse('blog_delete', args='1'))
        self.assertRedirects(post_response, reverse('blogs'), status_code=302)


    