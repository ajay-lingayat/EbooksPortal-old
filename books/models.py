from django.db import models

# Create your models here.
class book(models.Model):
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
    date = models.DateField(auto_now_add=True)
    downloads = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ep_book'
        verbose_name = 'book'
        verbose_name_plural = 'books'

class book_section(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'ep_book_section'
        verbose_name = 'book section'
        verbose_name_plural = 'book sections'