# posts/urls.py
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.MovieList.as_view()),
    path('<int:pk>/', views.MovieDetail.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]