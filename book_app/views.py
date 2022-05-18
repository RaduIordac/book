from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.urls import reverse

from book_app.forms import BookForm, AuthorForm
from book_app.models import Book, Author


def home_view(request):
    return render(request, template_name='home.html')

def show_books_view(request):
    return render(request, template_name= "books.html", context={"context_books" : Book.objects.all()})

def create_book(request):
    if request.method == "GET":
        form = BookForm()
        author_form = AuthorForm()
        content = loader.render_to_string("create_books.html", {"form": form, "author_form": author_form}, request)

        return HttpResponse(content)
    elif request.method == "POST":
        form = BookForm(data=request.POST)
        author_form = AuthorForm(data=request.POST)
        if form.is_valid() and author_form.is_valid():

            try:
                author = Author.objects.get(first_name=author_form.cleaned_data["first_name"],
                                            last_name=author_form.cleaned_data["last_name"])
            except Author.DoesNotExist:
                author = Author.objects.create(first_name=author_form.cleaned_data["first_name"],
                                            last_name=author_form.cleaned_data["last_name"])

            book = Book.objects.create(
                title=form.cleaned_data["title"],
                genre = form.cleaned_data["genre"],
                numbers_of_pages=form.cleaned_data["numbers_of_pages"],
                description=form.cleaned_data["description"],
                published=form.cleaned_data["published"],
                state = form.cleaned_data["state"],
            )
            # book.authors.set(form.cleaned_data["authors"])
            book.authors.add(author)
            # form.save()
            return redirect(reverse("books"))
        else:
            return render(request, template_name= "create_books.html", context={"form": form, "author_form": author_form})

