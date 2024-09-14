from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('blog/', views.Blog, name='blog'),
    path('<slug:slug>', views.single_post, name='single_post')
]
