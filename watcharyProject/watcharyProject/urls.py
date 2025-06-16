from django.contrib import admin
from django.urls import path

from watcharyProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('new/', new, name='new'),
    path('popular/', popular, name='popular'),
    path('search/', search, name='search'),
    path('signin/', sign_in, name='signin'),
    path('addMovies/', addMovies, name='addMovies')
]