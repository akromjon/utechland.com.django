from django.urls import path
from .controllers import blog, home, category, tag, about

urlpatterns = [
    #home page
    path('', home.index, name='home.index'),

    path('posts/', blog.index, name='post.index'),
    path('posts/<str:slug>', blog.show, name='post.show'),

    path('categories/', category.index, name='category.index'),
    path('categories/<str:slug>', category.show, name='category.show'),

    path('tags/', tag.index, name='tag.index'),
    path('tags/<str:slug>', tag.show, name='tag.show'),

    path('about/', about.index, name='about.index'),
]
