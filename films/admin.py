from django.contrib import admin
from .models import Films


class Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ['title']


admin.site.register(Films, Admin)
# Register your models here.
