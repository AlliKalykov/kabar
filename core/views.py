from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Post
from .forms import PostForm


class HomeView(TemplateView):
    template_name = 'home/home.html'


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/post.html'
    success_url = '/home/'
