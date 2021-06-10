import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
x_cor = data['x'].tolist()
y_cor = data['y'].tolist()

game_on = True
count = 0
correct_guess = []

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{count}/50 Guess the State", prompt="Enter State's Name")
    answer_state = answer.title()
    if answer_state == 'Exit':
        break
    if answer_state in states:
        correct_guess.append(answer_state)
        count += 1
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        x_dist = x_cor[states.index(answer_state)]
        y_dist = y_cor[states.index(answer_state)]
        name.goto(x_dist, y_dist)
        name.write(answer_state)


states_to_learn = []
for state in states:
    if state not in correct_guess:
        states_to_learn.append(state)

print(states_to_learn)
final = pandas.DataFrame(states_to_learn)
final.to_csv("states_to_learn")