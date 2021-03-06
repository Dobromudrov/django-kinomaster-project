from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import *
from .forms import *


class GenreNav:
    def get_genres(self):
        return Genre.objects.all()


class IndexPage(GenreNav, ListView):
    """Main page with movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "main_page/index.html"


class MovieDetail(GenreNav, DetailView):
    """Full description of movies"""
    model = Movie
    slug_field = "url"
    template_name = "main_page/movie_detail.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


class AddReview(View):
    """Review of the film"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        # print(request.POST)
        return redirect(movie.get_absolute_url())


class FilterMoviesView(GenreNav, ListView):
    template_name = "main_page/index.html"

    def get_queryset(self):
        queryset = Movie.objects.filter(
            # Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset


class JsonFilterMoviesView(ListView):
    template_name = "main_page/index.html"
    """Фильтр фильмов в json"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            # Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
