from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'store'

urlpatterns = [
    path('',views.home, name="home"),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
]

