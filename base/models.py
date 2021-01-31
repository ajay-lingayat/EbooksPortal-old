from django.db import models
from django.contrib.auth.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

from books.models import *
from papers.models import *

from simple_history.models import HistoricalRecords
from ConsoleMessenger import ConsoleMessage

global CMD
CMD = ConsoleMessage()

# Create your models here.
SECTION_CATEGORY = [
    ('books', 'Books'),
    ('papers', 'Papers'),
    ('both', 'Books & Papers')
]

USER_THEME = [
    ('light', 'Light'),
    ('dark', 'Dark')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    theme = models.CharField(max_length=20, choices=USER_THEME, default='light')
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'ep_profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

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

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        if created:
            Profile.objects.create(user=instance).save()
    except Exception as err:
        CMD.danger(err)