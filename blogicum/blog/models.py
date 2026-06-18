from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AbstractModel(models.Model):
    is_published = models.BooleanField(
        blank=False, 
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        blank=False, 
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True

class Post(AbstractModel):
    title = models.CharField(
        max_length=256, 
        blank=False,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        blank=False,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — ' \
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        blank=False,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        'Location', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=False,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
    
class Category(AbstractModel):
    title = models.CharField(
        max_length=256, 
        blank=False,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        blank=False,
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True, 
        blank=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; ' \
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

class Location(AbstractModel):
    name = models.CharField(
        max_length=256, 
        blank=False,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'