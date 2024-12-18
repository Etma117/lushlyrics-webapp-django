from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Mainpage

urlpatterns = [
    path('', Mainpage.as_view(), name='mainpage'),
    path("home", views.default, name='home'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page') 
]