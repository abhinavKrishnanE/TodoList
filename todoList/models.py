from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status_update = [("pending", "Pending"), ("complete", "Complete")]
    status = models.CharField(max_length=20, choices= status_update)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    
