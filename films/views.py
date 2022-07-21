from django.shortcuts import render, redirect
from films.models import Films
import random
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'films/hello.html')


def home(request):
    films = Films.objects.all()
    films = list(films)
    random.shuffle(films)
    films_aleatoire = random.sample(films, k=4)
    likes = {}
    for film in films:
        likes[film] = len(film.likeur.all())
    return render(request, 'films/home.html', {"likes": likes, "films_aleatoire": films_aleatoire})


class FilmDetail(DetailView):
    model = Films


@login_required
def add_favorite(request, film_id):
    le_film = Films.objects.filter(id=film_id).first()
    user = request.user
    if le_film in user.profile.films.all():
        messages.warning(request, 'that film {} is already in your favorites movies'.format(le_film.title))
    else:
        user.profile.films.add(le_film)
        user.profile.save()
        messages.success(request, 'that film {} is successfully added in your favorites movies'.format(le_film.title))

    return redirect('home')


@login_required
def mylist_favorite(request):

    films = Films.objects.filter(profile=request.user.profile)
    films = list(films)
    taille_mylist = len(films)
    return render(request, 'films/mylist_film.html', {'taille_mylist': taille_mylist, 'films': films})


@login_required
def remove_add_favorite(request, film_id):
    le_film = Films.objects.filter(id=film_id).first()
    user = request.user
    user.profile.films.remove(le_film)
    user.profile.save()
    messages.success(request, 'that film {} is successfully deleted in your favorites movies'.format(le_film.title))
    return redirect('list')


def liker(request, film_id):
    le_film = Films.objects.filter(id=film_id).first()
    user = request.user
    if user in le_film.likeur.all():
        messages.warning(request, 'that film {} has been liked by you'.format(le_film.title))
    else:
        le_film.likeur.add(user)
        le_film.save()
        messages.success(request, 'that film {} is successfully added in your liked movies'.format(le_film.title))

    return redirect('home')

#########################################CRUD sur film########################################################
"""def home(request):

    films = Films.objects.all()
    films = list(films)
    random.shuffle(films)
    films_aleatoire = random.choices(films, k=4)
    likes = {}
    for film in films:
        likes[film] = len(film.likeur.all())
    return render(request, 'films/home.html', {"likes": likes, "films_aleatoire": films_aleatoire})


class FilmDetail(DetailView):
    model = Films"""


class FilmCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Films
    fields = ['title', 'description', 'image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FilmUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Films
    fields = ['title', 'description', 'image']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FilmDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Films
    success_url = "/"

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False




# Create your views here.
