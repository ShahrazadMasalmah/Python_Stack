from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return ('Hi ' + name + '!')

@app.route('/repeat/<int:id>/<name>')
def repeat_id(id, name):
    return (f"{name}\n"*int(id))

@app.errorhandler(404)
def wrong_url(e):
    return "Sorry! No response. Try again." 
  
if __name__ == '__main__':
    app.run(debug=True)