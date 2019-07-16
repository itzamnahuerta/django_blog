from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = " Welcome "
    context = {"title": title}
    if request.user.is_authenticated:
        context = {"title": title, "my_list": [1,2,3,4,5,6]}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})
    
def contact_page(request):
    print(request.POST)
    return render(request, "form.html", {"title": "Contact Us"})

def example_page(request):
    context         = {"title": "Example"}
    template_name   = "hello_world.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))
        