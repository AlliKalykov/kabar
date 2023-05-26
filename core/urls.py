from django.urls import path
from .views import HomeView, PostView, CategoryView, SubCategoryView, TagView, PostListView, PostDetailView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post-create/', PostView.as_view(), name='post-create'),
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category-create/', CategoryView.as_view(), name='category-create'),
    path('subcategory-create/', SubCategoryView.as_view(), name='subcategory-create'),
    path('tag-create/', TagView.as_view(), name='tag-create'),

]
