from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie', 'time_create')
    list_display_links = ('name', 'movie')


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {"url": ("name",)}


class DirectorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Directors, DirectorsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews, ReviewsAdmin)

# class CarsTableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'cat', 'is_published', 'price', 'photo', 'time_create', 'time_update', 'slug')
#     list_display_links = ('id', 'title', 'cat')
#     search_fields = ('id', 'title',)
#     list_editable = ('is_published', 'price')
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(CarsTable, CarsTableAdmin)