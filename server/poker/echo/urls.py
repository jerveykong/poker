from django.conf.urls import patterns, url

from echo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getUser/$', views.getUser, name='getUser')
)
