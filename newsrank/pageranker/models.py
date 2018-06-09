from django.db import models
from django.utils import timezone

# Create your models here.

class Vote(models.Model):
    TYPES_OF_VOTE_CHOICES = (
        ('fake','Fake News'),
        ('true', 'The Real Truth'),
        # ('?','Not sure')
    )
    
    vote = models.CharField(max_length = 40,choices=TYPES_OF_VOTE_CHOICES,default = 'fake')     
    ip = models.CharField(max_length = 200,null=True, blank=True)
    url = models.CharField(max_length = 200)
    host = models.CharField(max_length = 200)
    vote_time = models.DateTimeField(default=timezone.now)
    meta = models.CharField(max_length = 200)
    