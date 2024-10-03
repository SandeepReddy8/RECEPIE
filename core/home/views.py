from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    peoples=[
        {'name':'sandeep','age':77},
        {'name':'Reddy','age':17},
        {'name':'ajay','age':71},
        {'name':'rashmi','age':99},
        {'name':'boss','age':7},
]
    text=['sandeep','daddy','rashmi']
    for people in peoples:
        print(people)
    return render (request, "index.html",context ={'page':'home','peoples': peoples,'text':text})
def sucess_page(request):
    return HttpResponse("hey ytjis is ASUCESS PAGE.")
def contact(request):
    context={'page':'contact'}
    return render (request, "contact.html",context)
def about(request):
    context={'page':'about'}
    return render (request, "about.html",context)