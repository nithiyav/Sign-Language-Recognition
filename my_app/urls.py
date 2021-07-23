from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import *
from . import views

urlpatterns = [
                path('prediction', PredictionAPIView.as_view()),

                path('', views.home, name = 'home'),
                path('result', views.result, name = 'result'),
                path('predict', views.predict, name = 'predict'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)