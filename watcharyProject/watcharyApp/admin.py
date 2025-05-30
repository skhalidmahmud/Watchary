from django.contrib import admin

# Register your models here.
from watcharyApp.models import Movie, TVSeries, Episode

admin.site.register(Movie)
admin.site.register(TVSeries)
admin.site.register(Episode)