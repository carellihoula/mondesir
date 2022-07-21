from django.contrib import admin
from django.urls import path
from .views import \
    (index,
     home,
     FilmDetail,
     add_favorite,
     mylist_favorite,
     remove_add_favorite,
     liker,
     FilmCreateView,
     FilmUpdateView,
     FilmDeleteView,)

urlpatterns = [
    path('index/', index, name="index"),
    path('', home, name="home"),
    path('films/<int:pk>', FilmDetail.as_view(template_name='films/film_detail.html'), name="film-detail"),
    path('film-new/', FilmCreateView.as_view(template_name="films/film_form.html"), name="film-new"),
    path('film/<int:pk>/update', FilmUpdateView.as_view(template_name="films/film_form.html"), name="film-update"),
    path('film/<int:pk>/delete', FilmDeleteView.as_view(template_name="films/film_confirm_delete.html"), name="film-delete"),
    path('favorite/<int:film_id>', add_favorite, name="favorite"),
    path('remove/<int:film_id>', remove_add_favorite, name="remove_favorite"),
    path('mylist/', mylist_favorite, name="list"),
    path('like/<int:film_id>', liker, name="liker"),
]