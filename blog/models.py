from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_details', args=[str(self.id)]) ## this will redirect me to details page(view)