from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self) -> str:
        return f'{self.name}'


class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategories')

    def __str__(self) -> str:
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')

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
