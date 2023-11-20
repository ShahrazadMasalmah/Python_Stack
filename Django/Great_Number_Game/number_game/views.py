from django.shortcuts import render, redirect, HttpResponse
import random
import _markupbase
def safe_number(request):
    random_number = random.randint(1, 100)
    print(random_number)
    request.session["random_number"] = random_number
    if "count" not in request.session:
        request.session["count"] = 1
    else:
        request.session["count"] += 1
        print(request.session["count"])
    return render(request, "index.html")

def compare(request):
    print(request.POST)
    counter = request.session["count"]
    if counter > 4:
        request.session["count"] = 0
        context = {
                "string" : "You Lose!",
                "color" : "#f71e16",
                "reset_button" : ''
            }  
        return render(request, "index.html", context)
    else:
        number = request.POST["number"]
        if abs(int(number) - request.session["random_number"]) > 5:
            context = {
                "string" : "Too low!",
                "color" : "#cf2a27",
                "reset_button" : ''
            }  
            return render(request, "index.html", context)
        elif abs(int(number) - request.session["random_number"]) == 0:
            reset_button ='<input type="text" name="playername"><input type="submit" name="go" value="Go">'
            context = {
                "string" : f"{number} was the number!",
                "color" : "#009e0f",
                "reset_button" : reset_button
            }     
            return render(request, "index.html", context)
        elif abs(int(number) - request.session["random_number"]) < 5: 
            context = {
                "string" : "Too high!",
                "color" : "#cf2a27",
                "reset_button" : ''
            }    
            return render(request, "index.html", context)


def try_again(request):
    return redirect("/")

def show_result(request):
    counter = request.session["count"]
    request.session["count"] = 0
    name = request.POST["playername"]
    context = {
                "name" : name,
                "counter" : counter
            }  
    return render(request, "show.html", context)
