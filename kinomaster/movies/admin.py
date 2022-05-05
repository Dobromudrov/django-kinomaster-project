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


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'movie')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie', 'time_create')
    list_display_links = ('name', 'movie')


# class CarsTableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'cat', 'is_published', 'price', 'photo', 'time_create', 'time_update', 'slug')
#     list_display_links = ('id', 'title', 'cat')
#     search_fields = ('id', 'title',)
#     list_editable = ('is_published', 'price')
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(CarsTable, CarsTableAdmin)