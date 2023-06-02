from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy

from .models import Post, Category, SubCategory, Tag, Comment
from .forms import PostForm, CategoryForm, SubCategoryForm, TagForm, CommentForm


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
        # get params from url
        params = request.GET
        
        # get params from url
        tag = params.get('tag')
        subcategory = params.get('subcategory')
        category = params.get('category')

        # filter posts
        if tag:
            posts = Post.objects.filter(tags__name=tag)
            context = {
                'posts': posts
            }
            return render(request, self.template_name, context)
        elif subcategory:
            posts = Post.objects.filter(subcategory__name=subcategory)
            context = {
                'posts': posts
            }
            return render(request, self.template_name, context)
        elif category:
            posts = Post.objects.filter(subcategory__category__name=category)
            context = {
                'posts': posts
            }
            return render(request, self.template_name, context)
        
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
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        context = {
            'post': post,
            'form': form,
            'comments': comments
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


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'core/comment.html'
    
    # def success redirect
    def get_success_url(self) -> str:
        return reverse_lazy('post-detail', kwargs={'pk': self.request.POST.get('post')})


# 3. Добавьте модель Comment с полями:
#     - post (ForeignKey(Post))
#     - author (ForeignKey(User)) - автор комментария, нужно использовать модель User из django.contrib.auth.models
#     - text (TextField)
#     - created_at (DateTimeField) - дата создания комментария

# 4. Добавьте модель Comment в админку
# 5. В админке Post выведите количество комментариев для каждого поста
# 6. Добавьте view для создания комментария
# 7. Добавьте view для просмотра списка комментариев, по постам