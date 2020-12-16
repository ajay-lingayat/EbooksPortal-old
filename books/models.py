from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=500)
    attachment = models.URLField(max_length=200)
    image = models.URLField(
        max_length=200,
        default='https://github.com/Ajay2810-hub/Ebooks/raw/master/default/images/image_unavailable.jpg'
    )
    tags = models.URLField(
        max_length=200,
        default='https://github.com/Ajay2810-hub/Ebooks/blob/master/default/tags/tag.txt'
    )
    create_date = models.DateField(auto_now_add=True)
    downloads = models.BigIntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ep_book'
        verbose_name = 'book'
        verbose_name_plural = 'books'

class BookSection(models.Model):
    text = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'ep_book_section'
        verbose_name = 'book section'
        verbose_name_plural = 'book sections'