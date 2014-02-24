from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Meeting, AgendaItem, Alert


def index(request):
    meetings = Meeting.objects.all()
    return render(request, 'agendas/index.html',
                  {'meetings': meetings})


def alert(request):
    if 'POST' == request.method:
        item = get_object_or_404(AgendaItem, pk=request.POST.get('agenda_item'))
        alert = Alert(item=item, phone=request.POST.get('tel'), sent=False)
        alert.save()
        return HttpResponse(status_code=201)
