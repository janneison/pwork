from django.conf.urls import url, include
from . import views

urlpatterns = [
   # url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
       url(r'^$', views.index_view, name='seguridad.index'),
    url(r'^login/$', views.login_view, name='seguridad.login'),
    url(r'^logout/$', views.logout_view, name='seguridad.logout'),
    url(r'^perfil/$', views.profile_view, name='seguridad.perfil'),
     url(r'^trabajo/$', views.trabajo_list, name='trabajo_list'),
    url(r'^trabajo/(?P<pk>[0-9]+)/$', views.trabajo_detail, name='trabajo_detail'),
    url(r'^trabajo/new/$', views.trabajo_new, name='trabajo_new'),
    url(r'^trabajo/(?P<pk>[0-9]+)/edit/$', views.trabajo_edit, name='trabajo_edit'),
]