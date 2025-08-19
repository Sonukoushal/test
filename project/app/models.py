from django.db import models

class Sonu(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
