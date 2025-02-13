from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    






class Post(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    summary=models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    