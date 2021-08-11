from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/login', methods=["GET","POST"])
def receive_data():
    return f"<h1>Name: {request.form['username']} and Pass: {request.form['password']}</h1>"

if __name__ == "__main__":
    app.run(debug=True)