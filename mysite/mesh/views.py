from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os

def index(request):
    filepath = 'index.html'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def mtl(request):
    filepath = 'mesh/mesh.mtl'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def obj(request):
    filepath = 'mesh/mesh2.obj'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def jpeg(request):
    filepath = 'mesh/mesh.jpeg'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def js(request, filename):
    filepath = 'js/' + filename + '.js'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
