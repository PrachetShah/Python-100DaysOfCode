from flask import Flask

app = Flask(__name__)

@app.route("/")
def greeting():
    return '<body>' \
           '<h1 style="text-align:center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
           '</body>'

random_number = 5
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img alt='elon-musk' src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/U52j0YphKRTEs/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)