from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = "__all__"


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
    list_display = ("title", "category", "year", "time_movies", "get_poster", "time_create", "time_update", "draft")
    prepopulated_fields = {"url": ("title", "year")}
    list_filter = ("category", "year",)
    search_fields = ("title", "category__name")
    list_editable = ("draft",)
    readonly_fields = ("get_poster",)
    form = MovieAdminForm
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
            "fields": (("poster", "get_poster" ), )
        }),
    )
    inlines = [ReviewInline]
    save_on_top = True

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90 height="80"')

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


admin.site.site_title = "Кабинет Разработчика [KinoMaster]"
admin.site.site_header = "Кабинет Разработчика [KinoMaster]"
