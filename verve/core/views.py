from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Event, Activities, Registration, Contact, Testimonial, Gallery
from datetime import datetime

# Create your views here.
def main(request):
    upcoming_gigs = Event.objects.filter(date__gte = datetime.now())
    highligts = Event.objects.filter(date__lt = datetime.now())

    return render(request, "index.html", {
        "upcoming_gigs" : upcoming_gigs,
        "highligts": highligts
    })

def contact(request):
    contacts = Contact.objects.all()
    return render(request, "contact.html",{
        "contacts":contacts
    })

def event(request, id):
    event = Event.objects.get(id=id)
    activities = Activities.objects.filter(event=event)

    return render(request, "event.html",{
        "event": event,
        "activities": activities
    })

def gallery(request, year):
    gallery = Gallery.objects.filter(year__year=year)
    events = Event.objects.filter(date__year=year)
    gallery_vid = [obj.video.url for obj in gallery]
    gallery_img = [obj.image.url for obj in gallery]
    images = [event.img.url for event in events]
    videos = [event.vid.url for event in events]
    
    return render(request, "gallery.html", {
        "year": year,
        "gallery_vid": gallery_vid,
        "gallery_img": gallery_img,
        "images":images,
        "videos": videos,
    })

def registration(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        participant_name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        gender = request.POST.get('gender')
        college = request.POST.get('college') 

        if not all([participant_name, email, department, gender]):
            return JsonResponse({'error': 'All fields are required!'}, status=400)
        
        registration = Registration.objects.create(
            event=event,
            participant_name=participant_name,
            email=email,
            department=department,
            gender=gender,
            college=college,
        ).save()

        print(request.POST)

        return JsonResponse({'success': 'Registration successful!'}, status=200)

    return render(request,"registration.html", {
        "event":event,
    })

def about(request):
    testimonials = Testimonial.objects.all()
    return render(request,"about.html", {
        "testimonials":testimonials
    })