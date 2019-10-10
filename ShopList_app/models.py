from django.db import models

class NewList(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item
