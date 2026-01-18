from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'Warzone/home.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'Warzone/blog_detail.html', {'blog': blog})

def home(request):
    
    
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request,'Warzone/home.html',{'blogs': blogs});

def robots_txt(request):
    robots_path = os.path.join(settings.STATICFILES_DIRS[0], 'robots.txt')
    try:
        with open(robots_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/plain')
    except (FileNotFoundError, IndexError):
        # Fallback if robots.txt not found or STATICFILES_DIRS is empty
        return HttpResponse('User-agent: *\nDisallow: /admin/\n\nSitemap: https://greystandardktm.com/sitemap.xml', content_type='text/plain')

