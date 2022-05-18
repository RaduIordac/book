from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)

    # def __str__(self):
    #     f"{self.name[]}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    class State(models.IntegerChoices):
        READ = 1
        NOT_READ = 2
        ONGOING = 3

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    numbers_of_pages = models.IntegerField()
    description = models.TextField()
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=State.choices)

    def __str__(self):
        return f"ID: {self.id} - Title: {self.title} - Authors : {self.author}"


