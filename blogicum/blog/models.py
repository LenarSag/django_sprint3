from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedAndCreatedModel


User = get_user_model()


class Category(PublishedAndCreatedModel):
    title = models.CharField("Заголовок", max_length=256)
    description = models.TextField("Описание")
    slug = models.SlugField(
        "Идентификатор",
        unique=True,
        help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
    )
    verbose_name = "категория"
    verbose_name_plural = "Категории"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class Location(PublishedAndCreatedModel):
    name = models.CharField("Название места", max_length=256)

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"


class Post(PublishedAndCreatedModel):
    title = models.CharField("Заголовок", max_length=256)
    text = models.TextField("Текст")
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text="Если установить дату и время в будущем — можно делать отложенные публикации.",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор публикации",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"