from django.db import models
from django.contrib.auth.models import User
from films.models import Films

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    films = models.ManyToManyField(Films)


def __str__(self):
    return self.user.username
