from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {"url": ("name",)}


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


class ReviewInline(admin.TabularInline):
    # StackedInline/TabularInline
    model = Reviews
    extra = 1
    readonly_fields = ("name", "text")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "time_movies", "draft", "time_create", "time_update")
    prepopulated_fields = {"url": ("title",)}
    list_filter = ("category", "year",)
    search_fields = ("title", "category__name")
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("title", "url", "draft"), )
        }),
        (None, {
            "fields": (("category", ), )
        }),
        (None, {
            "fields": (("country", "time_movies", "year" ), )
        }),
        (None, {
            "fields": (("genres", ), )
        }),
        (None, {
            "fields": (("actors", "directors"), )
        }),
        (None, {
            "fields": (("description",), )
        }),
        (None, {
            "fields": (("poster",), )
        }),
    )
    inlines = [ReviewInline]
    save_on_top = True

    # title = models.CharField("Название", max_length=100)
    # poster = models.ImageField("Постер", upload_to="movies/")
    # year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    # country = models.CharField("Страна", max_length=30)
    # category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    # genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    # time_movies = models.PositiveSmallIntegerField("Продолжительность (мин)", default=120)
    # directors = models.ForeignKey(Directors, verbose_name="Режиссёр", on_delete=models.CASCADE, null=True)
    # actors = models.ManyToManyField(Actors, verbose_name="Актёры", related_name="film_actor")
    # description = models.TextField("Описание")
    # url = models.SlugField(max_length=160, unique=True)
    # draft = models.BooleanField("Черновик", default=False)


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("value",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip", "star", "movie")


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "movie", "time_create")
    list_display_links = ("movie",)
    readonly_fields = ("name",)



# class CarsTableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'cat', 'is_published', 'price', 'photo', 'time_create', 'time_update', 'slug')
#     list_display_links = ('id', 'title', 'cat')
#     search_fields = ('id', 'title',)
#     list_editable = ('is_published', 'price')
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(CarsTable, CarsTableAdmin)