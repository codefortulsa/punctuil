from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'punctuil_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('agendas.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
