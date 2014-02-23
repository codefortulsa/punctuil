from django.shortcuts import render

from .models import Meeting


def index(request):
    meetings = Meeting.objects.all()
    return render(request, 'agendas/index.html',
                  {'meetings': meetings})
