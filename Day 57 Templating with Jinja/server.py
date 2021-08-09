from flask import Flask, render_template
from datetime import datetime
import requests

date = datetime.now()

app = Flask(__name__)

@app.route('/')
def home():
    year = date.year
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()
    age = age["age"]
    result = requests.get(f"https://api.genderize.io?name={name}")
    gender = result.json()
    gender = gender["gender"]
    return render_template('predict.html',name=name, gender=gender,age=age)

@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/e5aa94ce16fc572668e3")
    all_posts = response.json()
    return render_template('blog.html',posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)