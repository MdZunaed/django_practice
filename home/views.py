from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Zunayed', 'age': 21},
        {'name': 'Zubaer', 'age': 25},
        {'name': 'Mokhles', 'age': 16},
        {'name': 'Salam', 'age': 17},
        {'name': 'Borkot', 'age': 65},
    ]
    return render(request, "home/index.html",context= {'peoples': peoples })

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def success_page(request):
    return HttpResponse("This is success page")
