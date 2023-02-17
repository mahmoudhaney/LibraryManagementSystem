from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method == "POST":
        book_data = BookForm(request.POST, request.FILES)
        if book_data.is_valid():
            book_data.save()

        category_data = CategoryForm(request.POST)
        if category_data.is_valid():
            category_data.save()

    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'book_form': BookForm(),
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)

def delete(request):
    context = {
        'categories': Category.objects.all(),
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/delete.html', context)

def update(request, id):
    bood_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_data = BookForm(request.POST, request.FILES, instance=bood_id)
        if book_data.is_valid():
            book_data.save()
            return redirect('/')
    else:
        book_data = BookForm(instance=bood_id)

    context = {
        'update_form': book_data,
    }
    return render(request, 'pages/update.html', context)