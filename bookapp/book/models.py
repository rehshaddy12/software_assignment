from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()


    def __str__(self):
        return self.title


#my addition start here @elikana
class User:
    def __init__(self, username: str, password: str):
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        self.username = username
        self.password = password


class BookManagement:
    def __init__(self):
        self.users = {}

    def sign_up(self, username: str, password: str):
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username, password)
        self.users[username] = user
        return user
#my addition end here @elikana
