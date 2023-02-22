from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('iru', views.IruView, name='iru'),
    path('vmgo', views.VmgoView, name='vmgo'),
    path('about', views.aboutView, name='about'),
    path('gallery', views.GallaryView, name='gallery')
]
