from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("gallery", views.gallery, name="gallery"),
    path("registration", views.registration, name="registration"),
    path("event", views.event, name="event"),
]