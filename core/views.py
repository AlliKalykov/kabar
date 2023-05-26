from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Post, Category, SubCategory, Tag
from .forms import PostForm, CategoryForm, SubCategoryForm, TagForm


class HomeView(TemplateView):
    template_name = 'home/home.html'


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/post.html'
    success_url = '/home/'


class PostListView(ListView):
    model = Post
    template_name = 'core/post-list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, self.template_name, context)
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post-detail.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        context = {
            'post': post
        }
        return render(request, self.template_name, context)


class CategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'core/post.html'
    success_url = '/home/'


class TagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'core/post.html'
    success_url = '/home/'


class SubCategoryView(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'core/post.html'
    success_url = '/home/'
