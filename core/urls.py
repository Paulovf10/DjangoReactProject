from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, UserProfileListView, \
    UserProfileRetrieveView, EquipeCreateView, EquipeListView, EquipeUpdateView, EquipeDeleteView, EquipeRetrieveView, \
    MetaCreateView, MetaUpdateView, MetaListView, MetaDeleteView, MetaRetrieveView, AtualizacoesMetaListView, \
    AtualizarMetaCreateView

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = u'Administração'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('api/auth/', include('custom_auth.api_urls')),
    path('user/create/', UserProfileCreateView.as_view(), name='gestor-create'),
    path('user/update/<int:pk>/', UserProfileUpdateView.as_view(), name='gestor-update', ),
    path('user/list/', UserProfileListView.as_view(), name='gestor-list'),
    path('user/delete/<int:pk>/', UserProfileDeleteView.as_view(), name='gestor-delete'),
    path('user/retrieve/<int:pk>/', UserProfileRetrieveView.as_view(), name='gestor-retrieve'),

    path('equipe/create/', EquipeCreateView.as_view(), name='equipe-create'),
    path('equipe/update/<int:pk>/', EquipeUpdateView.as_view(), name='equipe-update', ),
    path('equipe/list/', EquipeListView.as_view(), name='equipe-list'),
    path('equipe/delete/<int:pk>/', EquipeDeleteView.as_view(), name='equipe-delete'),
    path('equipe/retrieve/<int:pk>/', EquipeRetrieveView.as_view(), name='equipe-retrieve'),

    path('meta/create/', MetaCreateView.as_view(), name='meta-create'),
    path('meta/update/<int:pk>/', MetaUpdateView.as_view(), name='meta-update', ),
    path('meta/list/', MetaListView.as_view(), name='meta-list'),
    path('meta/delete/<int:pk>/', MetaDeleteView.as_view(), name='meta-delete'),
    path('meta/retrieve/<int:pk>/', MetaRetrieveView.as_view(), name='meta-retrieve'),

    path('meta/<int:meta_id>/atualizacoes/', AtualizacoesMetaListView.as_view(), name='atualizacoes-meta-list'),
    path('meta/<int:meta_id>/atualizar/', AtualizarMetaCreateView.as_view(), name='atualizar-meta-create'),

    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]
