from flask import Flask,render_template,request,redirect
app = Flask(__name__)
@app.route('/')
def fromPage ():
    return render_template('index.html')
# 
@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    name =request.form['userName']
    location = request.form['dojoLocations']
    language = request.form['FavoritetLanguage']
    comment= request.form['comment']
    Gender=request.form['Gender']
    vehicle=request.form['vehicle1']
    return render_template('show.html',userName=name, dojoLocations=location,FavoritetLanguage= language,comments=comment,Gender=Gender,vehicle=vehicle)


if __name__=="__main__":
    app.run(debug=True)