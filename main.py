import turtle
import pandas

screen = turtle.Screen()
screen.setup(1400,1400)
screen.title('Poland Voivodeships Game')
image = 'poland-map.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv('16_voivodeships.csv')
all_voivodeships = data['voivodeship'].to_list()

guessed_voivodeships = []

while len(guessed_voivodeships) < 16:
    player_answer = screen.textinput(title=f'{len(guessed_voivodeships)}/16 Voivodeships Correct',
                                     prompt= 'What is another voivodeship name?').lower()

    if player_answer in all_voivodeships:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        voivodeship_data = data[data.voivodeship == player_answer]
        t.goto(int(voivodeship_data.x), int(voivodeship_data.y))
        t.write(player_answer,  font=("Arial", 16, "normal"))

# turtle.mainloop()
screen.exitonclick()
