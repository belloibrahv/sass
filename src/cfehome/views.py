import pathlib
# from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page(requests, *args, **kwargs):
    return about_page(requests, *args, **kwargs)

def about_page(requests, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=requests.path)
    
    try: 
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0

    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percentage": percent, 
    }
    html_ = ""
    html_template = "home.html"
    path = html_template
    print(path)
    PageVisit.objects.create()
    return render(requests, html_template, my_context)