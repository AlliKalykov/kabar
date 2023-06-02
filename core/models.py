from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    # subcategories = поле обратной связи
    # subcategories.posts = поле обратной связи через подкатегорию

    def __str__(self) -> str:
        return f'{self.name}'


class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategories')

    # posts = поле обратной связи

    def __str__(self) -> str:
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    
    # posts = поле обратной связи

    def __str__(self) -> str:
        return f'{self.name}'
    

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Подкатегория', related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='posts')
    poster = models.ImageField(upload_to='posters', verbose_name='Постер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self) -> str:
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', related_name='comments', null=True)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self) -> str:
        return f'{self.author} - {self.post}'
    
    class Meta:
        ordering = ['-post', '-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'