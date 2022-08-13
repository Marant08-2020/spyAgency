from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('hitmen', views.ListHitmenDetails, name='listhitmendetails'),
    path('hitmen/update', views.ListHitmenChange, name='edithitmen'),
    path('hitmen/<int:_id>', views.HitmanDetails, name='detail_hitman'),
    path('hitmen/update/<pk>', views.UpdateHitMan.as_view(), name='updater_hitman'),
    path('register/mangers', views.MangerRegister.as_view(), name='manager_register'),
    path('register/hitman', views.HitManRegister.as_view(), name='hitmam_register'),
]

