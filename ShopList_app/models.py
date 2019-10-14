from django.db import models

class List(models.Model):
    list_name = models.TextField()
    def __str__(self):
        return self.list_name
