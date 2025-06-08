from django.shortcuts import render

import requests 
from django.core import serializers


def index(request):
    return render(request, "index.html")

