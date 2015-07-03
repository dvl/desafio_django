# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FilmeListView.as_view(), name='index'),
    url(r'^filme/(?P<slug>[-\w]+)/$', views.FilmeDetailView.as_view(), name='filme'),
    url(r'^ator/(?P<slug>[-\w]+)/$', views.AtorDetailView.as_view(), name='ator'),
    url(r'^genero/(?P<slug>[-\w]+)/$', views.FilmeListView.as_view(), name='genero'),
]
