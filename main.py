import turtle
import pandas

screen = turtle.Screen()
screen.setup(1400,1400)
screen.title('Poland Voivodeships Game')
image = 'poland-map.gif'
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()