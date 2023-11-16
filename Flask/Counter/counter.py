from flask import Flask , render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def create_counter():
    if "count" not in session:
        print("There is no key!")
        session["count"] = 1
    else:
        print("The key exists!")
        session["count"] += 1    
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    session.pop('key_name', None)
    return redirect('/')

@app.route('/count', methods=['POST'])
def Increment_by_two():
    if request.form['submit'] == "add":
        session["count"] += 1
    elif request.form['submit'] == "reset":
        session["count"] = 0    
    return redirect('/') 


if __name__ == '__main__':
    app.run(debug=True)