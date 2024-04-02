from flask import Flask, render_template, request
from calculator import Calculate

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/checkNew", methods=["POST", "GET"])
def account():
    if request.method == "POST":
        operation = request.form.get("operation")
        x = float(request.form.get("x", 0))  # Default to 0 if not provided
        y = float(request.form.get("y", 0))  # Default to 0 if not provided
        
        calc = Calculate(x, y)
        result = "<Invalid Operation>"
        
        if operation == "add":
            result = calc.add()
        elif operation == "subtract":
            result = calc.subtract()
        elif operation == "multiply":
            result = calc.multiply()
        elif operation == "divide":
            result = calc.divide()

        return render_template("checkNew.html", result=result)
    else:
        # If not POST, just render the form again
        return render_template("home.html")


if __name__ == "__main__": #checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)
