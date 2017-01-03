from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^przewoznicy$', views.PrzewoznicyListView.as_view(), name='Lista przewoźników'),
    url(r'^linie$', views.LinieListView.as_view(), name='Lista linii'),
    url(r'^autobusy$', views.AutobusyListView.as_view(), name='Lista autobusów'),
    url(r'^tramwaje$', views.TramwajeListView.as_view(), name='Lista tramwajów'),
    url(r'^kierowcy$', views.KierowcyListView.as_view(), name='Lista kierowców'),
    url(r'^motorniczy$', views.MotorniczyListView.as_view(), name='Lista motorniczych'),
    url(r'^przystanki$', views.PrzystankiListView.as_view(), name='Lista przystnaków'),
]
