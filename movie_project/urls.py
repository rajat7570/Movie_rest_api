# movie_project/urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),

]
