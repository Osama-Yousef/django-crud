from django.urls import path
from .views import BlogListView, BlogDetailView ,BlogCreateView ,BlogUpdateView ,BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),   
    path('post/new/', BlogCreateView.as_view(), name='blog_create'), 
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),

]
