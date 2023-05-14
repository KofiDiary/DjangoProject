from django.shortcuts import render
from .models import warehouse

# Create your views here.

def index(request):
    return render(request, 'Warehouse/index.html', {
        'Warehouse': warehouse.objects.all()
    })