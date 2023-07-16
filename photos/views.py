from django.shortcuts import render

from django.contrib.auth.models import User

def gallery(request):
    return render(request, 'photos/gallery.html')


def addPhoto(request):
    return render(request, 'photos/add.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')
