from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    sum = int(strawberry) + int(raspberry) + int(apple)
    print(f"Charging {firstName} {lastName} for {sum} fruits.")
    
    return render_template("checkout.html",sum=sum, strawberry=strawberry, raspberry=raspberry, apple=apple, 
                           firstName=firstName, lastName=lastName, studentId=studentId)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    