from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexPage.as_view()),
    path("<int:pk>/", views.MovieDatail.as_view()),
]