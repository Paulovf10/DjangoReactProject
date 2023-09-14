from django.contrib import admin
from django.urls import path, include
from . import views as auth_views
from .views import UserAPIView

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = u'Administração'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('', UserAPIView.as_view()),

    path('save-address/', auth_views.save_address, name='save_address'),
    path('set-principal-address/', auth_views.set_principal_address, name='set_principal_address'),
    path('get-principal-address/', auth_views.get_principal_address, name='get_principal_address'),
    path('register/', auth_views.registration_view, name='api_register'),
    path('login/', auth_views.login_view, name='api_login'),
    path('check/', auth_views.check_user_view, name='api_check_user'),
    path('change-password/', auth_views.change_user_password, name='api_change_password'),

]
