"""
Este archivo define las rutas principales del proyecto mi_blog.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as blog_views
from cuentas import views as accounts_views  # Importa las vistas de 'cuentas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('cuentas.urls')),  # Incluye las URLs de la app 'cuentas'
    path('blogs/', include('blogs.urls')),  # Incluye las URLs de la app 'blogs'
    path('mensajes/', include('mensajes.urls')),  # Incluye las URLs de la app 'mensajes'
    path('about/', blog_views.about, name='about'),  # Ruta para la página "Acerca de mí"
    path(
        'pages/', blog_views.pages, name='pages'
    ),  # Ruta para listar las páginas de blogs
    path(
        'pages/<int:page_id>/', blog_views.page_detail, name='page_detail'
    ),  # Ruta para el detalle de cada página
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
