from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        """The Author item model."""
        return f'{self.name}: {self.email}'

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    dateOfCreation = models.DateField()
    deadline = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        """The ToDo item model."""
        return self.title