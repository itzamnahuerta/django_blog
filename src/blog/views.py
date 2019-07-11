from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail_page.html'
    context = {"object": obj} 
    return render(request, template_name, context)


# GET = RETRIVE/LIST
# POST = CREATE/UPDATE/DELETE

def blog_post_list_view(request):
    return 

def blog_post_create_view(request):
    return 

def blog_post_retrieve_view(request):
    return 

def blog_post_update_view(request):
    return 

def blog_post_delete_view(request):
    return 

    