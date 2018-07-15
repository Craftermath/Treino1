from django.db import models
from django.db.models import CASCADE


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField('Author', null=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    # publisher = models.ManyToManyField('Publisher') tanto faz aqui ou no Publisher (n to n)

    def get_random_number(self):
        return 9

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=CASCADE)  #  1 pra n colocar no n
    publisher = models.ForeignKey(Publisher, on_delete=CASCADE, null=True)  #  1 pra n colocar no n

# book = Book.objects.get(pk=1)
# book.author
#
# author = Author.objects.get(pk=1)
# author.book_set.all()  #  -> Book.objects.filter(author=1)