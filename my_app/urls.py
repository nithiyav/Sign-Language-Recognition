from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
                path('prediction', PredictionAPIView.as_view()),
]
