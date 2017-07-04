from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import re
import base64
import os
from . import recog
import subprocess
import json
import jsonpickle
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
    filepath = 'mesh/mesh.obj'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def jpeg(request):
    filepath = 'mesh/mesh.jpeg'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def js(request, filename):
    filepath = 'js/' + filename + '.js'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def upload(request):
    #print(request.POST.dict())
    dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
    image = dataUrlPattern.match(request.POST.dict()['img_1']).group(2);
    Image_bin = base64.b64decode(image)
    with open("file_1.jpeg", "wb+") as fd:
        fd.write(Image_bin)
    image = dataUrlPattern.match(request.POST.dict()['img_2']).group(2);
    Image_bin = base64.b64decode(image)
    with open("file_2.jpeg", "wb+") as fd:
        fd.write(Image_bin)

    l = recog.to_list_of_results("file_1.jpeg", "file_2.jpeg")
    a = jsonpickle.encode(l)
    return HttpResponse(a, content_type="application/json")