from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = "hello there ...  "
    return render(request, "hello_world.html", {"title":title})

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})
    
def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))
        