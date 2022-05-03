from datetime import datetime
from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length = 150)
    artist = models.CharField(max_length = 150)
    duration = models.FloatField()
    last_play = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    