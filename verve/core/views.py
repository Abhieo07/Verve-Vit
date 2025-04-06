from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Event, Activities, Registration, Contact, Testimonial, Gallery, Carousel
from datetime import datetime

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import qrcode
import base64
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the image to a base64 string
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

def registration(request, id):
    event = get_object_or_404(Event, id=id)
    category = event.category
    vid_url = Carousel.objects.get(category=category).vid_reg.url

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
        )

        # Generate QR Code
        qr_data = f"""
        Event: {event.title}
        Participant: {participant_name}
        Email: {email}
        Date: {event.date}
        Venue: {event.location}
        """
        qr_b64 = generate_qr_code(qr_data)

        # PDF Generation
        context = {
            'event': event,
            'registration': registration,
            'qr_code': qr_b64,
        }
        
        html_string = render_to_string('ticket_pdf.html', context)
        pdf_file = HTML(string=html_string).write_pdf()
        
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{event.title}_ticket.pdf"'
        registration.save()
        return response

    return render(request, "registration.html", {
        "event": event,
        "vid_url": vid_url,
    })

# Create your views here.
def main(request):
    upcoming_gigs = Event.objects.filter(date__gte = datetime.now())
    highligts = Event.objects.filter(date__lt = datetime.now())
    carousel_vid = Carousel.objects.all()

    return render(request, "index.html", {
        "upcoming_gigs" : upcoming_gigs,
        "highligts": highligts,
        "sports_url":carousel_vid.get(category="Sports").vid_carousel.url,
        "cultural_url":carousel_vid.get(category="Cultural").vid_carousel.url,
        "technical_url":carousel_vid.get(category="Technical").vid_carousel.url,
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
    gallery_vid = [obj.video.url for obj in gallery]
    gallery_img = [obj.image.url for obj in gallery]
    
    return render(request, "gallery.html", {
        "year": year,
        "gallery_vid": gallery_vid,
        "gallery_img": gallery_img,
    })

# def registration(request, id):
#     event = get_object_or_404(Event, id=id)
#     category = event.category
#     vid_url = Carousel.objects.get(category=category).vid_reg.url

#     if request.method == 'POST':
#         participant_name = request.POST.get('name')
#         email = request.POST.get('email')
#         department = request.POST.get('department')
#         gender = request.POST.get('gender')
#         college = request.POST.get('college') 

#         if not all([participant_name, email, department, gender]):
#             return JsonResponse({'error': 'All fields are required!'}, status=400)
        
#         registration = Registration.objects.create(
#             event=event,
#             participant_name=participant_name,
#             email=email,
#             department=department,
#             gender=gender,
#             college=college,
#         ).save()

#         print(request.POST)

#         return JsonResponse({'success': 'Registration successful!'}, status=200)

#     return render(request,"registration.html", {
#         "event":event,
#         "vid_url":vid_url,
#     })

def about(request):
    testimonials = Testimonial.objects.all()
    return render(request,"about.html", {
        "testimonials":testimonials
    })