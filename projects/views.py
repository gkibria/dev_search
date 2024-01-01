from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):
    all_items = Project.objects.all()
    # first_item = Project.objects.first()
    # last_item = Project.objects.last()
    # latest_item = Project.objects.latest()

    # return all_items

    print(all_items)
