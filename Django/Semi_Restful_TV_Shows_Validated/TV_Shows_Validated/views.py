from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def goTo(request):
    return redirect("/shows")

def adding_Tv_Show(request):
    return render(request, "TvShow.html")

def createShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:        
        title = request.POST['title']
        network  = request.POST['network'] 
        release_date = request.POST['date']
        description = request.POST['description']
        this_show = Show.objects.create(title = title, network = network, release_date = release_date, description = description)
        return redirect(f"/shows/{this_show.id}")
        

def showDetail(request, id):
    this_show = Show.objects.get(id=id)
    context = {
        "this_show" : this_show,
    }
    return render(request, "showDetail.html", context)

def showTable(request):
    context = {
        "shows" : Show.objects.all()
    } 
    return render(request, "showTable.html", context) 

def edit(request, id):
    this_show = Show.objects.get(id=id)
    context = {
        "this_show" : this_show
    }
    return render(request, "editShow.html", context)  

def showChange(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:    
        this_show = Show.objects.get(id=id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['date']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect(f"/shows/{this_show.id}")

def delete(request, id):
    this_show = Show.objects.get(id=id)
    this_show.delete()
    return redirect("/shows")      