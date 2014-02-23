from django.db import models


# Create your models here.
class Meeting(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    agenda_id = models.CharField(max_length=200, unique=True)


class AgendaItem(models.Model):
    meeting = models.ForeignKey(Meeting)
    section = models.TextField(blank=True)
    number = models.IntegerField()
    text = models.TextField()
    minutes = models.TextField(blank=True)
    backup = models.TextField(blank=True)
