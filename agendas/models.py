from django.db import models


# Create your models here.
class Meeting(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    agenda_id = models.CharField(max_length=200, unique=True)


class AgendaItem(models.Model):
    meeting = models.ForeignKey(Meeting, related_name='items')
    section = models.TextField(blank=True)
    number = models.IntegerField()
    text = models.TextField()
    minutes = models.TextField(blank=True)
    backup = models.TextField(blank=True)


class Alert(models.Model):
    item = models.ForeignKey(AgendaItem, related_name='alerts')
    phone = models.CharField(max_length=12)
    sent = models.BooleanField(default=False)
