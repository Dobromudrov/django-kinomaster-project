from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    prepopulated_fields = {"url": ("name",)}
    search_fields = ("name",)


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    search_fields = ("name",)


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
    list_display = ("title", "category", "year", "time_movies", "get_poster", "draft", "time_create", "time_update")
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
            "fields": (("poster", ), )
        }),
    )
    inlines = [ReviewInline]
    save_on_top = True

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50 height="60"')

    get_poster.short_description = "Изображение"


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
    readonly_fields = ("name", "movie", "text")



# class CarsTableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'cat', 'is_published', 'price', 'photo', 'time_create', 'time_update', 'slug')
#     list_display_links = ('id', 'title', 'cat')
#     search_fields = ('id', 'title',)
#     list_editable = ('is_published', 'price')
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(CarsTable, CarsTableAdmin)

admin.site.site_title = "Кабинет Разработчика [KinoMaster]"
admin.site.site_header = "Кабинет Разработчика [KinoMaster]"
