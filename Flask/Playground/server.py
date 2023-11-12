from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "go to http://localhost:5000/play to have it do something "

@app.route("/play")
def render():
    return render_template("index.html")

@app.route("/play/<X>", methods=['GET'])
def render_id(X):
    return render_template("index2.html", num = int(X))

@app.route("/play/<X>/<color>", methods=['GET'])
def render_id_color(X, color):
    return render_template("index3.html", num = int(X), color = color)

if __name__ == "__main__":
    app.run(debug=True)