from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def event(request):
    return render(request, "event.html")

def gallery(request):
    return render(request, "gallery.html")

def registration(request):
    return render(request,"registration.html")

def about(request):
    return render(request,"about.html")