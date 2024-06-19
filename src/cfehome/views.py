import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def hello_home_page(requests, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=requests.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percentage": (page_qs.count() * 100) / qs.count(),
    }
    html_ = ""
    html_template = "home.html"
    path = html_template
    print(path)
    PageVisit.objects.create()
    return render(requests, html_template, my_context)
