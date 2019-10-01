from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.index),
    url(r'^evento/(?P<id>.*)$',  views.evento),
    url(r'^admision/$',  views.admision),
    url(r'^actividades/$',  views.actividades),
    url(r'^descargas/$',  views.descargas),
    url(r'^somos/$',  views.somos),
    url(r'^especialistas/$',  views.especialistas),
    url(r'^send-email/', views.send_email),
]