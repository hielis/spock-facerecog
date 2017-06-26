from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'mtl', views.mtl, name='mtl'),
    url(r'obj', views.obj, name='obj'),
    url(r'mesh.jpeg', views.jpeg, name='jpeg'),
    url(r'js/([0-9a-zA-Z/\.]+).js', views.js, name='js'),


]
