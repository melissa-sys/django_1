from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

# category_id número intenro que identifica a cada una de las filas de las tablas en la base de datos


def category(request, category_id):
    # get me eprmite coger solo un dato
    category = get_object_or_404(id=category_id)
    return render(request, 'blog/category.html', {'posts': posts})
