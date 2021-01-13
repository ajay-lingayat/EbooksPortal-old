from django.db import models
from django.contrib.auth.models import *

from books.models import *
from papers.models import *

from simple_history.models import HistoricalRecords

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ep_tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'