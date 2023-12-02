from django.db import models
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "The first name should be at least 2 characters!"

        if not postData['first_name'].isalpha():
            errors['first_name'] = "The first name should be just letters!"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "The last name should be at least 2 characters!" 

        if not postData['last_name'].isalpha():
            errors['last_name'] = "The last name should be just letters!"    

        if len(postData['email']) == 0 or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!" 

        if len(postData['birthday']) == 0:
            errors['birthday'] = "There is no birthday date!" 

        if postData['birthday']:
            birthday_date = datetime.strptime(postData['birthday'], '%Y-%m-%d').date()
            current_date = timezone.now().date()
            if birthday_date >= current_date - relativedelta(years=13):
                errors["birthday"] = "Birthday date must be in the past and the user age must be at least 13!"         

        if len(postData['password']) < 8:
           errors['password'] = "The password should be at least 8 characters!" 

        if  postData['confirm_password'] !=  postData['password']:
             errors['confirm_password'] = "The confirmation of password does not match the password!"

        return errors  
    def login_validate(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if len(postData['email']) == 0 or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!" 

        if len(postData['password']) < 8:
           errors['password'] = "The password should be at least 8 characters!" 
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField() 
    message = models.ForeignKey(Message, related_name="comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   