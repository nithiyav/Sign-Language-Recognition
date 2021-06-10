from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
                path('prediction', PredictionAPIView.as_view()),

                path('', views.home, name = 'home'),
]
