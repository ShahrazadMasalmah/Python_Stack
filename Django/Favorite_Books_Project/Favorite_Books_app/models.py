from django.db import models
import re
import bcrypt 

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name should be at least 2 characters and letters!"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name should be at least 2 characters and letters!"
        if len(postData['last_name']) == 0 or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!" 
        if len(postData['password']) < 8:
            errors["password"]="Password must be at least 8 characters!"
        if postData['password'] != postData['confirm_password']:
            errors["password"]="Passwords do not match!"
        return errors  

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = "Must enter an email!"
        if len(User.objects.filter(email=postData['email'])) == 0:
            errors['email'] = "Email is not registered!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        elif bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()) != True:
            errors['password'] = "Password is incorrect!" 
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title book must be at lesat 3 characters!"
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at lesat 5 characters!"               
        return errors            


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_liked = models.ManyToManyField(User, related_name="liked_books") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()   