from django.db import models

class List(models.Model):
    list_name = models.TextField()
    def __str__(self):
        return self.list_name

class Item(models.Model):
    item_name = models.TextField()
    item_done = models.BooleanField(default=False)
    item_list = models.ForeignKey(List,default=None, on_delete=models.PROTECT)
    def __str__(self):
        return self.item_name