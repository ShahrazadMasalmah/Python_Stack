from django.shortcuts import render, redirect
import random
import datetime

def show_gold(request):
    if "gold_count" not in request.session:
        request.session["gold_count"] = 0
    if "activity" not in request.session:
        request.session["activity"] = []

    activity_comment = request.session["activity"]
    gold_count = request.session["gold_count"]
    context = {
        "activity_comment" : activity_comment,
        "gold_count" : gold_count,
    }     
    return render(request, "index.html", context)


def process_gold(request):
    if request.POST['building'] == "farm":
        farm_gold = random.randint(10, 20)
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {farm_gold} golds from the house! ({times})</p>"
        request.session["activity"].append(event)
        request.session.save()
        request.session["gold_count"] += farm_gold
        
    if request.POST['building'] == "cave":
        cave_gold = random.randint(5, 10)
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {cave_gold} golds from the house! ({times})</p>"
        request.session["activity"].append(event)
        request.session.save()
        request.session["gold_count"] += cave_gold

    if request.POST['building'] == "house":
        house_gold = random.randint(2, 5) 
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {house_gold} golds from the house! ({times})</p>"
        request.session["activity"].append(event)
        request.session.save()
        request.session["gold_count"] += house_gold

    if request.POST['building'] == "casino":
        random_number = random.randrange(1,3)
        if random_number == 1:    
            casino_gold = random.randint(0, 50)
            now = datetime.datetime.now()
            times = now.strftime("%B %d %Y %I:%M %p")
            event = f"<p class='greentext'>Earned {casino_gold} golds from the house! ({times})</p>"
            request.session["activity"].append(event)
            request.session.save()
            request.session["gold_count"] += casino_gold

        if random_number == 2:    
            casino_gold = random.randint(0, 50)
            now = datetime.datetime.now()
            times = now.strftime("%B %d %Y %I:%M %p")
            event = f"<p class='redtext'>Earned {casino_gold} golds from the house! ({times})</p>"
            request.session["activity"].append(event)
            request.session.save()
            request.session["gold_count"] -= casino_gold
            
    return redirect("/")

def destroy(request):
    request.session["gold_count"] = 0
    request.session["activity"] = []
    return redirect("/")