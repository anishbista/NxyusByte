from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    published_date = models.DateField()

    class Meta:
        ordering = ["published_date"]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
