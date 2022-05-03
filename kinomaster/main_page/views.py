from django.shortcuts import render
from django.views.generic.base import View

from movies.models import *


class IndexPage(View):
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, "main_page/index.html", {"movie_list": movies})
