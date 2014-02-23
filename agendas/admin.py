from django.contrib import admin

from agendas.models import Meeting, AgendaItem

# Register your models here.
admin.site.register(Meeting)
admin.site.register(AgendaItem)
