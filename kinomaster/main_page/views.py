from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import *


class IndexPage(ListView):
    """Main page with movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "main_page/index.html"


class MovieDetail(DetailView):
    """full description of movies"""
    model = Movie
    slug_field = "url"
    template_name = "main_page/movie_detail.html"
