from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model
# Create your models here.

class Post(models.Model):
    Title = models.Charfield(max_lenght=250)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
