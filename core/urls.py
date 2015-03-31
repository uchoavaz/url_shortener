from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'core.views.cadastre', name='cadastre'),
    url(r'^detalhes/(?P<slug>[\w_-]+)/$', 'core.views.details', name='details'),
    url(r'^pesquisa/(?P<slug>[\w_-]+)/$', 'core.views.redirectUrl', name='redirectUrl'),

)
