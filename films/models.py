from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Films(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='films_pic')
    likeur = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("film-detail", kwargs={"pk": self.pk})