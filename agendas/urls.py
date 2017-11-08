from django.conf.urls import url

from agendas import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agendas/alert$', views.alert, name='alert')
]
