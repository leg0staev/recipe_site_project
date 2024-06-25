from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

# Получение модели пользователя
User = get_user_model()


class Category(models.Model):
    """
    Модель Категорий на сайте
    """
    title = models.CharField(max_length=255, verbose_name='Название', unique=True)

    def __str__(self):
        return f"#{self.pk}. {self.title}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


class Recipe(models.Model):
    """
    Модель рецептов на сайте
    """

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления (минут)', default=0)
    img = models.ImageField(upload_to='recipe', blank=True, null=True, verbose_name='Изображение', validators=[
        FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, verbose_name='Категории')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    added_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'
