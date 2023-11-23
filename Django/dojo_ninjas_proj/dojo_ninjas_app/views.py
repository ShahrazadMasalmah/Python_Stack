from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def show(request):       
    context = {"dojos" : Dojo.objects.all(), 
    }
    return render(request, "index.html", context)

def createDojo(request):
    name = request.POST['name'] 
    city = request.POST['city']
    state = request.POST['state'] 
    Dojo.objects.create(name=name, city=city, state=state)
    return redirect("/")

def createNinja(request):
    firstName = request.POST['first_name']  
    lastName = request.POST['last_name']
    dojo_name = request.POST['dojo']
    Ninja.objects.create(first_name=firstName, last_name=lastName, dojo=Dojo.objects.get(name=dojo_name))
    return redirect("/")

def deleteDojoNinjas(request):
    dojo = Dojo.objects.get(id=request.POST['submit'])
    dojo.ninjas.all().delete()
    dojo.delete()
    return redirect("/")


