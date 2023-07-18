from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photos.object.all()
    context = { "categories" : categories,"photos":photos }
    return render(request, 'photos/gallery.html', context)


def addPhoto(request):
    return render(request, 'photos/add.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')
