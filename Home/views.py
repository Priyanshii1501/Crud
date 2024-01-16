from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def index(Request):
    context = {
        'variable' : "this is sent"
    }
    return render(Request , "index.html" , context)
     #return HttpResponse("this is home page...")

def about(Request):
    return HttpResponse("this is About page...")

def services(Request):
    return HttpResponse("this is Service page...")

def contact(Request):
   if Request.method == "POST":
       name=Request.POST.get('name')  
       email = Request.POST.get('email')
       desc = Request.POST.get('desc')
       contact = Contact(name=name , email=email  , desc=desc, date=datetime.today())
       contact.save()
       messages.success(Request, "your msg has been sent!")
       



   return render(Request , "contact.html" )
