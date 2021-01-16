from django.db import models
from django.contrib.auth.models import *

from books.models import *
from papers.models import *

from simple_history.models import HistoricalRecords

# Create your models here.
SECTION_CATEGORY = [
    ('books', 'Books'),
    ('papers', 'Papers')
]

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ep_tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ('name',)

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    books = models.ManyToManyField(Book, blank=True)
    papers = models.ManyToManyField(Paper, blank=True)
    category = models.CharField(max_length=20, choices=SECTION_CATEGORY, default='books')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ep_section'
        verbose_name = 'section'
        verbose_name_plural = 'sections'
        ordering = ('name',)