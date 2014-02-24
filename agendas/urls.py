from django.conf.urls import patterns, url

from agendas import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^agendas/alert$', views.alert, name='alert')
)
