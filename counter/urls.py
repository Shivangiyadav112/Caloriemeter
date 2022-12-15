
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('exercise.html',views.exercise,name="exercise")
]