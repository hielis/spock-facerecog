from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os

def index(request, id):
    filepath = ""
    if(id == "0"):
        filepath = 'front.html'
    elif (id == "1"):
        filepath = 'right_side.html'
    elif(id == "2"):
        filepath = 'left_side.html'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def side(request):
    filepath = 'side.html'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def mtl(request):
    filepath = 'mesh/mesh.mtl'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def obj(request):
    filepath = 'mesh/sphere.obj'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def jpeg(request):
    filepath = 'mesh/mesh.jpeg'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def js(request, filename):
    filepath = 'js/' + filename + '.js'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
