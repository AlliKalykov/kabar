from django.urls import path
from .views import HomeView, PostView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post-create/', PostView.as_view(), name='post-create'),
]
