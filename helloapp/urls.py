from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.hello_json, name='hello_json'),
    path('html/', views.hello_html, name='hello_html'),
]

