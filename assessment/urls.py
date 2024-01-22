from django.urls import path
from .views import MovieListView, MovieDetailView, movieFormView

app_name = "legal"
urlpatterns = [
    path("list/", MovieListView.as_view(), name="list"),
    path("<int:pk>/detail/", MovieDetailView.as_view(), name="detail"),
    path("update/", movieFormView, name="update"),
]
