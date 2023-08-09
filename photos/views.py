from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = { "categories" : categories,"photos":photos }
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    Photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo':Photo})

def addPhoto(request):
    categories = Category.objects.all()

    context = { "categories" : categories,}
    return render(request, 'photos/add.html', context)