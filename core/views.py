from django.shortcuts import render, get_object_or_404
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
    # context_object_name = 'posts'

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
        post = get_object_or_404(Post, pk=kwargs['pk'])
        # post = Post.objects.get(pk=kwargs['pk'])
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
