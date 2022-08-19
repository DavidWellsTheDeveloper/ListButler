from django.db import models
from django.conf import settings

# Create your models here.
class List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    shared = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"

class ListItem(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    list = models.ForeignKey(
        List,
        related_name='list_items',
        on_delete=models.CASCADE
    )
    addedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.text}"