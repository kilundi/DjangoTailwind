from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
from main.models import Team

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name= "comments", on_delete=models.CASCADE)


class Client(models.Model):
    team = models.ForeignKey(Team, related_name='client', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'CLIENTS'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

    def number_of_comments(self):
        return self.comments.count()

class Todolist(models.Model):
    client = models.ForeignKey(Client, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    created_by = models.ForeignKey(User, related_name= "todolists", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)



class MyModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

    def __str__(self):
        return self.name

def get_currencies():
        return settings.CURRENCIES


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=get_currencies)