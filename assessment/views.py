from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class MovieListView(LoginRequiredMixin, ListView):
    login_url = "/"

    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetailView(LoginRequiredMixin, DetailView):
    login_url = "/"
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required(login_url="/")
def movieFormView(request):
    
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'assessment/movie_form.html', context)