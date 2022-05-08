from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("filter/", views.FilterMoviesView.as_view(), name="filter"),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", views.MovieDetail.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]