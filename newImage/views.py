
from django.shortcuts import render

# Create your views here.
from appofimage .models import *


def show_category(request, cid):
    cats = category.objects.all()

    cat = category.objects.get(pk=cid)

    images = post.objects.filter(cat=cat)

    data = {'images': images, 'cats': cats}

    return render(request, 'home.html', data)