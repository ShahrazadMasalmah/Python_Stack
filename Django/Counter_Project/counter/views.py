from django.shortcuts import render, redirect

def counter(request):
    if "countOne" and "countTwo" and "total" not in request.session:
        request.session["countOne"] = 1
        request.session["countTwo"] = 0
        request.session["total"] = 1
    else:
        request.session["countOne"] += 1 
        request.session["total"] += 1 

    return render(request, "index.html")

def destroy_session(request):
    del request.session['countOne']	# clears a specific key
    del request.session["countTwo"]
    del request.session['total']
    return redirect("/")  

def reset_add(request):
    if request.POST['submit'] == "reset":
        return redirect("/destroy_session")

    elif request.POST['submit'] == "add":
        number = request.POST['number']
        request.session["countTwo"] += int(number)
    request.session["total"] = request.session["countOne"] + request.session["countTwo"]
    return redirect("/") 



