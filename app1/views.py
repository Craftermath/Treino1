from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from app1.models import Author, Book, Publisher


def list_authors(request):
    # Author.objects.create(name=request.GET['nome'], age=request.GET['idade'])
    if request.POST :
        nome = request.POST.get('variavel_1')
        idade = request.POST.get('variavel_2')
        Author.objects.create(name=nome, age=idade)

    authors = Author.objects.all()
    year = 2018
    context = {
        'authors' : authors,
        'year' : year,
        'color' : 'blue',
    }
    return render(request, 'app1/list_authors.html', context)


def list_book(request):
    if request.POST:
        title = request.POST.get("title")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        Book.objects.create(title=title, author_id=author, publisher_id=publisher)

    book = Book.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()

    context = {
        "book": book,
        "authors": authors,
        "publishers": publishers
    }

    return render(request, "app1/book_list.html", context)


def detail_authors(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except Exception as err:
        raise Http404("O autor que vc buscou não existe!")
    if request.POST:
        idade = request.POST.get('variavel_idade')
        author.age = idade
        author.save()

    context = {'author': author}
    return render(request, 'app1/detail_authors.html', context)


def detail_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Exception as err:
        raise Http404("O livro que vc buscou não existe!")

    if request.POST:
        titulo = request.POST.get("titulo_novo")
        pub = request.POST.get("pub")
        if titulo:
            book.title = titulo
        book.publisher_id = pub
        book.save()


    context = {
        "titulo_novo": book,
        "publishers": Publisher.objects.all()
    }

    return render(request, 'app1/detail_book.html', context)


def delete_authors(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except:
        raise Http404("O author que voce buscou nao existe")

    author.delete()
    return HttpResponseRedirect("/author/list/")


def list_pub(request):
    if request.POST:
        name = request.POST.get("name")
        Publisher.objects.create(name=name)

    pubs = Publisher.objects.all()
    context = {
        "publishers": pubs,
    }

    return render(request, "app1/list_pub.html", context)
