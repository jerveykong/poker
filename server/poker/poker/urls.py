from django.conf.urls import patterns, url

from poker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^lobby/$', views.index, name='index')
)
