from django.db import models
from django.db.models import CharField
from django.db.models.functions import Lower

from simple_history.models import HistoricalRecords

# Create your models here.
CharField.register_lookup(Lower)

class Paper(models.Model):
    title = models.CharField(max_length=500)
    attachment = models.URLField(max_length=200)
    image = models.URLField(
        max_length=200,
        default='https://github.com/Ajay2810-hub/Ebooks/raw/master/default/images/image_unavailable.jpg'
    )
    tags = models.ManyToManyField(
        'base.Tag', blank=True
    )
    create_date = models.DateField(auto_now_add=True)
    downloads = models.BigIntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ep_paper'
        verbose_name = 'paper'
        verbose_name_plural = 'papers'

class PaperSection(models.Model):
    name = models.CharField(max_length=50)
    papers = models.ManyToManyField(
        Paper,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ep_paper_section'
        verbose_name = 'paper section'
        verbose_name_plural = 'paper sections'