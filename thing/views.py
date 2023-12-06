from django.shortcuts import render
from .models import Thing

def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {'things': things})
