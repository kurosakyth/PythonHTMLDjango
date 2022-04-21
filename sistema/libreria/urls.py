from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),    
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#urls trae el html de views, entonces monta primero las views, para tener la dirección en la web.
#inicio es "" entonces no tiene problema && nosotros es la otra página. Al igual que libros, que es
#otra página, pero esta tiene una subpágina