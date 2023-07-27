from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = { "categories" : categories,"photos":photos }
    return render(request, 'photos/gallery.html', context)


def addPhoto(request, pk):
    Photo = Photo.objects.get(id=pk)
    context = { 'Photo':Photo }
    return render(request, 'photos/add.html', context)

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')
