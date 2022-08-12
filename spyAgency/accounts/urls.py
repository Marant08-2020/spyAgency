from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('register/assignmanager', views.assignManager, name='assingmanager'),
    path('register/mangers', views.MangerRegister.as_view(), name='manager_register'),
    path('register/hitman', views.HitManRegister.as_view(), name='hitmam_register'),
]

