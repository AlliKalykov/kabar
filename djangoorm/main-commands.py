from core.models import Post, Category, SubCategory, Tag

posts = Post.objects.all()
print('Количество постов = ', posts.count())
# all() - SELECT * FROM posts 
# all() - возвращает список всех записей в таблице, но по умолчанию имеет ограничение
# count() - SELECT COUNT(*) FROM posts
# count() - возвращает количество записей в таблице

posts = Post.objects.get(id=1)
# get() - SELECT * FROM posts WHERE id = 1
# get() - возвращает одну запись, если запись не найдена, то возникает исключение (DoesNotExist)
# get() - если записей больше одной, то возникает исключение (MultipleObjectsReturned)

posts = Post.objects.filter(id=1)
print('Количество постов по id 1 = ', posts.count())
# filter() - SELECT * FROM posts WHERE id = 1
# filter() - возвращает список записей, если запись не найдена, то возвращает пустой список

SubCategory.objects.filter(category__name="Футбол")
# filter() - SELECT * FROM subcategories INNER JOIN categories ON subcategories.category_id = categories.id WHERE categories.name = 'Футбол'
# Возрващает все подкатегории, у которых наименование категории "Футбол"


Tag.objects.create(name="Тег 1")
# create() - INSERT INTO tags (name) VALUES ('Тег 1')
# create() - создает запись в таблице и возвращает объект этой записи

## Создание записи свяанной таблицы (один ко многим) (ForeignKey)
category = Category.objects.get(id=1)
SubCategory.objects.create(name="Подкатегория 1", category=category)

Tag.objects.filter(id=1).update(name="Тег 2")
# update() - UPDATE tags SET name = 'Тег 2' WHERE id = 1
# update() - обновляет запись в таблице и возвращает количество обновленных записей

# еще один спобос обновления записи (обновление одной единственной записи)
tag = Tag.objects.get(id=1)
tag.name = "Тег 3"
tag.save()


# удаление записи
SubCategory.objects.filter(id=3).delete()
# filter().delete() - удаляет запись из таблицы и возвращает количество удаленных записей, при этом удаляются все записи, которые прошли фильтр. 
# В данном случае, если у данной подкатегории есть посты, то эту подкатегорию удалить не получится, так как у подкатегории есть связанные записи в другой таблице  и возникнет исключение (ProtectedError) (так как в on_delete установлено значение PROTECT)
SubCategory.objects.get(id=3).delete()
# get().delete() - удаляет запись из таблицы, если запись не найдена, то возникает исключение (DoesNotExist)

Category.objects.all().delete()

# Category.objects.all().delete() - удаляет все записи из таблицы и возвращает количество удаленных записей. Удаляет все связанные подкатегории, так как в on_delete установлено значение CASCADE.
# Если есть пост у какой-то подкатегории мы не можем удалить данную категорию, так как есть связь с постами и подкатегориям, где on_delete установлено значение PROTECT.