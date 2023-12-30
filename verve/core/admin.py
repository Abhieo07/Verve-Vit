from django.contrib import admin
from .models import Contact, Event, Highlight, Testimonial, Gallery, Registration, Guest

# Register your models here

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'role']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'location', 'price', 'description', 'incharge']

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'title', 'description']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'author_role']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'participant_name', 'participant_id', 'college', 'gender', 'department', 'email', 'phone']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'guest_name', 'affiliation']
