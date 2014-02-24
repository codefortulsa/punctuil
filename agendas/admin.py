from django.contrib import admin

from agendas.models import Meeting, AgendaItem, Alert

# Register your models here.
admin.site.register(Meeting)
admin.site.register(AgendaItem)
admin.site.register(Alert)
