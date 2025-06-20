from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visao/', views.visao, name='visao'),
    path('carreira/', views.carreira, name='carreira'),
    path('albuns/', views.albuns, name='albuns'),
    path('galeria/', views.galeria, name='galeria'),
    path('albuns/urias/', views.urias_album, name='urias_album'),
    path('albuns/furia/', views.furia_album, name='furia_album'),
    path('albuns/hermind/', views.hermind_album, name='hermind_album'),
] 