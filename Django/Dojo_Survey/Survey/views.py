from django.shortcuts import render

def root(request):
    return render(request, "index.html")

def display_result(request):
    print(request.POST)
    name = request.POST["userName"]
    location = request.POST["dojoLocations"]
    language = request.POST["FavoritetLanguage"]
    text = request.POST["comment"]
    gender = request.POST["Gender"]
    transport = request.POST["vehicle1"]

    context = {
        "name" : name,
        "location" : location,
        "language" : language,
        "text" : text,
        "gender" : gender,
        "transport" : transport
    }
    return render(request, "show.html", context)    