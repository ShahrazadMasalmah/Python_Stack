from flask import Flask ,render_template
app = Flask(__name__)
@app.route("/")
def checkboard ():
    return render_template ('index.html', num = 4, number = 4)

@app.route("/<int:x>")
def checkboard_num (x):
    return render_template ('index.html', num=int(x/2), number = 4)

@app.route("/<int:x>/<int:y>")
def checkboard_mult (x, y):
    return render_template ('index.html', num=int(x/2), number=int(y/2))

if __name__ == '__main__':
    app.run(debug=True)
