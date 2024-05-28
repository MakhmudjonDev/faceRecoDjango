# recognition/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(upload_to='images/')
    encoding = models.BinaryField()

    def __str__(self):
        return self.name
