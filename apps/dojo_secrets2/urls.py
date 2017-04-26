from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^secret$', views.secret),
    url(r'^loggout$', views.loggout),
    url(r'^addpost$', views.addpost),
    url(r'^delete/(?P<id>\d)+$', views.delete),
    url(r'^addlike/(?P<id>\d)+$', views.addlike),
    url(r'^mostpopular$', views.mostpopular)
]
