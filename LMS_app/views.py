from django.shortcuts import render, redirect, get_object_or_404
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
        'all_books': Book.objects.filter(active=True).count(),
        'sold_books': Book.objects.filter(status='sold').count(),
        'rented_books': Book.objects.filter(status='rented').count(),
        'available_books': Book.objects.filter(status='available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    searchedTitle = None
    if 'search_name' in request.GET:
        searchedTitle = request.GET['search_name']
        if searchedTitle:
            search = search.filter(title__icontains=searchedTitle)

    context = {
        'categories': Category.objects.all(),
        'books': search,
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)

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

def delete(request, id):
    delete_book_id = get_object_or_404(Book, id=id)
    if request.method == "POST":
        delete_book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')