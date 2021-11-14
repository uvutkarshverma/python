from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact
from datetime import datetime

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
       
        data = Contact(name=name,email = email, query = query)
        data.save()
        context = {
            "message" :"Thanks for contacting us. We will get back to you shortly"
        }
        return render(request, "index.html", context)

    return HttpResponse(render(request, "index.html"))