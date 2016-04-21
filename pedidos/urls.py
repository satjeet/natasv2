from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pedido/new/$', views.pedido_new, name='pedido_new'),
    url(r'^pedido/(?P<pk>\d+)/edit/$', views.pedido_edit, name='pedido_edit'),
    url(r'^pedido/(?P<pk>\d+)/$', views.pedido_detalle, name='pedido_detalle'),
    url(r'^semana/$', views.pedidos_semana, name='pedidos_semana'),
    url(r'^parahoy/$', views.pedidos_hoy, name='pedidos_hoy'),
    url(r'^tresdias/$', views.pedidos_tresdias, name='pedidos_tresdias'),
    # login personalizado
    # url(r'^login/$', views.user_login, name='login'),

    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # login y logout por defecto en django, esperan estar en templates/registration
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    #url(r'^logouto/$', 'django.contrib.auth.views.logout',{'template_name': 'registration/logged_out.html'}, name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/pedidos/'}, name='logout'),
    url(r'^logout_then_login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

]

url