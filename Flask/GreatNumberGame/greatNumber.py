from flask import Flask , render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = "great number game"

@app.route("/")
def safe_number():
    random_number = random.randint(1, 100)
    print(random_number)
    session["random_number"] = random_number
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
        print(session["count"])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def compare():
    print(request.form)
    counter = session["count"]
    if counter > 4:
        session["count"] = 0
        string = "You Lose"
        color = "#f71e16"
        return render_template("index.html", string=string, color=color, reset_button='')
    else:
        number = request.form["number"]
        if abs(int(number) - session["random_number"]) > 5:
            string = "Too low!"
            color = "#cf2a27"
            return render_template("index.html", string=string, color=color, reset_button='')
        elif abs(int(number) - session["random_number"]) == 0:
            string = f"{number} was the number!" 
            color = "#009e0f"   
            reset_button = Markup('<form action="/result" method="post"><input type="text" name="playername"><input type="submit" name="go" value="Go"></form>')
            return render_template("index.html", string=string, color=color, reset_button=reset_button)
        elif abs(int(number) - session["random_number"]) < 5:
            string = "Too high!"   
            color = "#cf2a27"      
            return render_template("index.html", string=string, color=color, reset_button='')

@app.route("/try")
def try_again():
    return redirect("/")

@app.route("/result", methods=["POST"])
def show_result():
    counter = session["count"]
    session["count"] = 0
    name = request.form["playername"]
    return render_template("show.html", name=name, counter=counter)


if __name__ == "__main__":
    app.run(debug=True)