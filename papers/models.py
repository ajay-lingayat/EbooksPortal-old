from django.db import models

# Create your models here.
class paper(models.Model):
    title = models.CharField(max_length=500)
    attachment = models.URLField(max_length=200)
    image = models.URLField(
        max_length=200,
        default='https://github.com/Ajay2810-hub/Ebooks/raw/master/default/images/image_unavailable.jpg'
    )
    tags = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Paper'

class paper_download(models.Model):
    paper = models.ForeignKey(
        paper,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.paper.title

    class Meta:
        verbose_name = 'Paper Download'

class paper_section(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Paper Section'