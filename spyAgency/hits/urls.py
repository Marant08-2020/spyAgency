from django.urls import path
from . import views


urlpatterns = [
    path('', views.showHits, name='home'),
    path('bulk/', views.bulk, name='bulk'),
    path('create', views.create_hits, name='create_hits'),
    path('<int:_id>', views.detailsHits, name='detail_hits'),
    path('update/<int:_id>', views.UpdateHits, name='update_hits'),

]
