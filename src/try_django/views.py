from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "hello_world.html")

def about_page(request):
    return HttpResponse("<h1> about us </h1>")
    
def contact_page(request):
    return HttpResponse("<h1> contact us </h1>")
            