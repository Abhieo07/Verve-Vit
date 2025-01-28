from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.main, name="main"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("gallery/<int:year>", views.gallery, name="gallery"),
    path("registration/<int:id>", views.registration, name="registration"),
    path("event/<int:id>", views.event, name="event"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)