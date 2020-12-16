from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=500)
    attachment = models.URLField(max_length=200)
    image = models.URLField(
        max_length=200,
        default='https://github.com/Ajay2810-hub/Ebooks/raw/master/default/images/image_unavailable.jpg'
    )
    tags = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)
    downloads = models.BigIntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ep_paper'
        verbose_name = 'paper'
        verbose_name_plural = 'papers'

class PaperSection(models.Model):
    text = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'ep_paper_section'
        verbose_name = 'paper section'
        verbose_name_plural = 'paper sections'