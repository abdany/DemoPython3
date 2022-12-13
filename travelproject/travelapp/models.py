from django.db import models


class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics')
    desc1 = models.TextField()

    def __str__(self):
        return self.name1

# Create your models here.
