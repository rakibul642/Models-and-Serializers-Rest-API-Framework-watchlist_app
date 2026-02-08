from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<pk>/', views.movie_detail),
]