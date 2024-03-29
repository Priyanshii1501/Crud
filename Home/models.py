from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=32)
    desc = models.CharField(max_length=255, default="Some default value")
    date = models.DateField()

    def __str__(self):
        return self.name