from django.db import models
from django.utils import timezone
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if Show.objects.filter(title=postData['title']).exists():
            errors['title'] = "A TV show with this title already exists"

        if len(postData['title']) < 5:
            errors['title'] = "The title of the show should be at least 5 characters!"

        if len(postData['network']) < 3:
            errors['network'] = "The network of the show should be at least 3 characters!"

        if len(postData['date']) == 0:
            errors["date"] = "There is no release date!" 

        if postData['date']:
            release_date = datetime.strptime(postData['date'], '%Y-%m-%d').date()
            current_date = timezone.now().date()
            if release_date >= current_date:
                errors["date"] = "Release date must be in the past!" 

        if postData['description'] and len(postData['description']) < 10:
            errors['description'] = "The description of the show should be at least 10 characters!" 
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
