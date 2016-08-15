from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cupcake(models.Model):
    name      = models.CharField(max_length=200)
    rating    = models.CharField(max_length=20)
    price     = models.FloatField()
    images    = models.ImageField(upload_to='images/cupcakes')
    writer    = models.ForeignKey(User)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name