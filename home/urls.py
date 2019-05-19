from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views
app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    re_path('project/(?P<slug>[\w-]+)/', views.project, name="project"),
]
