from django.shortcuts import render
from django.views.generic.base import View

from movies.models import *


class IndexPage(View):
    """"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "main_page/index.html", {"movie_list": movies})


class MovieDatail(View):
    """"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, "main_page/movie_datail.html", {"movie": movie})