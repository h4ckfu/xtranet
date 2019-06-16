from django.shortcuts import render

from . models import FrontPage

def front_page(request):
    front_page = FrontPage.objects
    return render(request, 'jobs/home.html', {'front_page':front_page})
