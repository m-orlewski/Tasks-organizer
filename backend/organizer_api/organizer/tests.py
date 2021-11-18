from django.test import TestCase
from .models import Author, ToDoItem

# Create your tests here.

class AddToDoItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='name1', email='name1@email.com')
        ToDoItem.objects.create(title='first item',
                            description='first description',
                            dateOfCreation='2021-11-16',
                            deadline='2021-11-17',
                            Author=Author.objects.get(id=1))
    
    def test_title_content(self):
        item = ToDoItem.objects.get(id=1)
        expected = f'{item.title}'
        self.assertEquals(expected, 'first item')
    
    def test_description_content(self):
        item = ToDoItem.objects.get(id=1)
        expected = f'{item.description}'
        self.assertEquals(expected, 'first description')

    def test_date_of_creation_content(self):
        item = ToDoItem.objects.get(id=1)
        expected = f'{item.dateOfCreation}'
        self.assertEquals(expected, '2021-11-16')

    def test_deadline_content(self):
        item = ToDoItem.objects.get(id=1)
        expected = f'{item.deadline}'
        self.assertEquals(expected, '2021-11-17')

    def test_author(self):
        item = ToDoItem.objects.get(id=1)
        author = Author.objects.get(id=1)
        self.assertEquals(item.Author, author)