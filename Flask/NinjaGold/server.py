from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "Golden Game"

@app.route('/')
def show_gold():
    if "gold_count" not in session:
        session["gold_count"] = 0
    if "activity" not in session:
        session["activity"] = [] 

    activity_comment = session["activity"]
    gold_count = session["gold_count"]      

    return render_template("index.html", activity_comment=activity_comment, gold_count=gold_count)

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == "farm":
        farm_gold = random.randint(10, 20)
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {farm_gold} golds from the house! ({times})</p>"
        session["activity"].append(event)
        session["gold_count"] += farm_gold

    if request.form['building'] == "cave":
        cave_gold = random.randint(5, 10)
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {cave_gold} golds from the house! ({times})</p>"
        session["activity"].append(event)
        session["gold_count"] += cave_gold

    if request.form['building'] == "house":
        house_gold = random.randint(2, 5) 
        now = datetime.datetime.now()
        times = now.strftime("%B %d %Y %I:%M %p")
        event = f"<p class='greentext'>Earned {house_gold} golds from the house! ({times})</p>"
        session["activity"].append(event)
        session["gold_count"] += house_gold

    if request.form['building'] == "casino":
        random_number = random.randrange(1,3)
        if random_number == 1:    
            casino_gold = random.randint(0, 50)
            now = datetime.datetime.now()
            times = now.strftime("%B %d %Y %I:%M %p")
            event = f"<p class='greentext'>Earned {casino_gold} golds from the house! ({times})</p>"
            session["activity"].append(event)
            session["gold_count"] += casino_gold

        if random_number == 2:    
            casino_gold = random.randint(0, 50)
            now = datetime.datetime.now()
            times = now.strftime("%B %d %Y %I:%M %p")
            event = f"<p class='redtext'>Earned {casino_gold} golds from the house! ({times})</p>"
            session["activity"].append(event)
            session["gold_count"] -= casino_gold
    session["activity"].sort(reverse=True)        
    return redirect("/")        

@app.route('/destroy', methods=['POST'])
def destroy():
    session["gold_count"] = 0
    session["activity"] = []     
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)