from django.shortcuts import render, redirect
from .models import Book,Author

def index(request):
    contex = {
        'all_book':Book.objects.all(),
    }
    return render(request, "index.html",contex)

def add_book (request):
    print(request.POST)
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
        )
    return redirect('/')

def book_disply(request, book_id ):
    context = {
        'book_to_display': Book.objects.get(id=book_id),
        'all_author':Author.objects.all(),
    }
    return render(request, 'books.html', context)

def add_book_author(request):
    print(request.POST)
    author = Author.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f"books/{request.POST['book_id']}")



def all_author(request):
    context = {
        'all_author': Author.objects.all(),
    }
    return render(request,'author.html', context)

def add_author (request):
    print(request.POST)
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')

def show_author (request , author_id):
    context = {
        'author_to_display': Author.objects.get(id=author_id),
        'all_book': Book.objects.all(),
    }
    return render(request, 'authors.html', context)



def add_author_book (request):
    print(request.POST)
    author = Author.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f"authors/{request.POST['author_id']}")
