from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog

class StaticViewSitemap(Sitemap):
    protocol = 'https'
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['store:home', 'store:blog_list']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    protocol = 'https'
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('store:blog_detail', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.created_at

