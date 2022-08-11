from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHits, name='home'),
    path('create', views.create_hits, name='create_hits'),

]
