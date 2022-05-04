from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import *
from .forms import *


class IndexPage(ListView):
    """Main page with movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "main_page/index.html"


class MovieDetail(DetailView):
    """Full description of movies"""
    model = Movie
    slug_field = "url"
    template_name = "main_page/movie_detail.html"


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
