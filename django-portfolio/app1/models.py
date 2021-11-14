from datetime import datetime
from django.db import models
import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    query = models.TextField(max_length= 500)
    date = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name