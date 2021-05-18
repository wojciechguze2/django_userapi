from .views import Register, Login, DlaZalogowanych
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('api/register/', Register.as_view(), name='register'),
    path('api/login/', Login.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/dlazalogowanych/' , DlaZalogowanych.as_view(), name='dlazalogowanych'),
]
