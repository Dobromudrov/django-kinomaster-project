from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actors(models.Model):
    """Актёры"""
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры"
        verbose_name_plural = "Актёры"
        # ordering = ["name"]


class Directors(models.Model):
    """Режиссёры"""
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссёры"
        verbose_name_plural = "Режиссёры"
        ordering = ["name"]


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    country = models.CharField("Страна", max_length=30)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    time_movies = models.PositiveSmallIntegerField("Продолжительность (мин)", default=120)
    directors = models.ForeignKey(Directors, verbose_name="Режиссёр", on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actors, verbose_name="Актёры", related_name="film_actor")
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзыв"""
    name = models.CharField("Пользователь", max_length=20)
    # name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    movie = models.ForeignKey(Movie, verbose_name="Отзыв на Фильм", on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"
        ordering = ['-time_create', 'name']