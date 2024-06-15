from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('movies/',views.movies,name='movies'),
    path('serials/',views.serials,name='serials'),
    path('advertisements/',views.advertisements,name='advertisements'),
    path('web_series/',views.web_series,name='web_series'),
]