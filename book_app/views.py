from django.shortcuts import render

# Create your views here.
from book_app.models import Book


def home_view(request):
    return render(request, template_name='home.html')

def show_books_view(request):
    return render(request, template_name= "books.html", context={"context_books" : Book.objects.all()})
