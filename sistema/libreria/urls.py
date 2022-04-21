from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),    
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
]
#urls trae el html de views, entonces monta primero las views, para tener la dirección en la web.
#inicio es "" entonces no tiene problema && nosotros es la otra página. Al igual que libros, que es
#otra página, pero esta tiene una subpágina