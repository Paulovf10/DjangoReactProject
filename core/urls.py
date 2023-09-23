from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import GestorCreateView, GestorUpdateView, GestorDeleteView, GestorListView

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = u'Administração'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('api/auth/', include('custom_auth.api_urls')),
    path('gestor/create/', GestorCreateView.as_view(), name='gestor-create'),
    path('gestor/update/<int:pk>/', GestorUpdateView.as_view(), name='gestor-update', ),
    path('gestor/list/', GestorListView.as_view(), name='gestor-list'),
    path('gestor/delete/<int:pk>/', GestorDeleteView.as_view(), name='gestor-delete'),
    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]
