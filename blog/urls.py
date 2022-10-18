


from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('get/<int:id>/', views.getlist, name='get')
]
