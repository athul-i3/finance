from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.IntegerField()
    is_admin=models.BooleanField(default=False,null=True)

class Expenses(models.Model):
        
        CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]
        name=models.CharField(max_length=140) 
        date=models.DateField()
        category=models.CharField(max_length=25,choices=CATEGORY_CHOICES)
        description = models.TextField(blank=True)
        amount = models.PositiveIntegerField()
        created_by = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(default=timezone.now)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
