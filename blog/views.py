from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Post


class BlogListView(ListView):
    template_name = 'blogs.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'blog_details.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'blog_create.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'blog_update.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'blog_delete.html'
    model = Post
    success_url = reverse_lazy('blogs') ## when i delete , i will be redirected to homepage