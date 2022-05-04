from django.contrib import admin
from .models import *


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie', 'time_create')
    list_display_links = ('name', 'movie')


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {"url": ("name",)}



admin.site.register(Category)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Directors)
admin.site.register(Genre)
admin.site.register(Movie)
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