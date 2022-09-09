import turtle
import time
import random

#NOTE this is one of my first games written in python, I am not updating this code for history purposes, but I will make a better and updated version eventually.

Size = 0.5

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.title('Turtle Tron')
    wn.bgcolor('black')
    wn.screensize(320,320)
    wn.setup(width=1200, height=950,startx=None,starty=None)
    wn.tracer(0)
    cyan_history = set()
    magenta_history = set()

    #Specials (Coming soon...)

    #Y grid lines
    grid_y = turtle.Turtle()
    x = -320
    for y_lines in range(80):
        grid_y.color('#2F4F4F')
        grid_y.penup()
        grid_y.goto(x, 320)
        grid_y.pendown()
        grid_y.goto(x, -320)
        grid_y.hideturtle()
        x += 8

    #X grid lines
    grid_x = turtle.Turtle()
    y = -320
    for x_lines in range(80):
        grid_x.color('#2F4F4F')
        grid_x.penup()
        grid_x.goto(320, y)
        grid_x.pendown()
        grid_x.goto(-320, y)
        grid_x.hideturtle()
        y += 8

    #Bike Initilization
    class magenta_bike_init(turtle.Turtle):
        def __init__(self, color, pensize, shape, speed):
            #Magenta Bike
            super().__init__(shape)
            self.color(color)
            self.pensize(pensize)
            self.speed(speed)

    magenta_bike = magenta_bike_init("#FF00FF", 3, "turtle", 8)
    magenta_bike.shapesize(stretch_wid=Size, stretch_len=Size, outline=1)
    magenta_bike.penup()
    magenta_bike.sety(224)
    magenta_bike.setheading(-90)
    magenta_bike.pendown()
    #
    class cyan_bike_init(turtle.Turtle):
        def __init__(self, color, pensize, shape, speed):
            #Cyan Bike
            super().__init__(shape)
            self.color(color)
            self.pensize(pensize)
            self.speed(speed)
    cyan_bike = cyan_bike_init("#00FFFF", 3, "turtle", 8)
    cyan_bike.shapesize(stretch_wid=Size, stretch_len=Size, outline=1)
    cyan_bike.penup()
    cyan_bike.sety(-224)
    cyan_bike.setheading(90)
    cyan_bike.pendown()
    
    #Score
    class score_system:
        def __init__(self):
            self.magenta_score = 0
            self.cyan_score = 0
        def mag_add_one(self):
            self.magenta_score += 1
        def cyan_add_one(self):
            self.cyan_score += 1
    one = score_system()
    score = turtle.Turtle()
    score.pensize(2)
    score.pencolor('White')
    score.penup()
    score.goto(0,340)
    score.pendown()
    score.write(f'Cyan {one.cyan_score}, Magenta {one.magenta_score}',align="center",font=("Courier", 24, "normal"))
    score.hideturtle()

    #Author
    name = turtle.Turtle()
    name.pensize(2)
    name.hideturtle()
    name.pencolor('White')
    name.penup()
    name.goto(0,320)
    name.pendown()
    name.write('Made By RedRiver559559',align='center',font=("Courier", 8, "normal"))
    #Controls
    info = turtle.Turtle()
    info.color('white')
    info.penup()
    info.goto(-460,230)
    info.pendown()
    info.write('Cyan Controls\nW = Up\nS = Down\nA = Left\nD = Right',align='Left',font=("Courier", 12, "normal"))
    info.penup()
    info.home()
    info.goto(500,230)
    info.pendown()
    info.write('Magenta Controls\n↑ = Up\n↓ = Down\n← = Left\n→ = Right',align='Right',font=("Courier", 12, "normal"))
    info.hideturtle()
    #border
    pen = turtle.Turtle()
    pen.color('White')
    pen.penup()
    pen.setposition(-320,-320)
    pen.pendown()
    pen.pensize(1)
    pen.shape('square')
    pen.hideturtle()
    for x in range(4):
        pen.forward(640)
        pen.left(90)
        wn.update()
    pen.penup()
    pen.goto(0,380)
    pen.pendown()
    pen.pencolor('#2F4F4F')
    pen.write('Turtle Tron',align="center",font=("Courier", 48, "normal"))




#Controls (Up, Down, Left, Right)
#checking if it can reverse in the opposite x or y direction vs its current pos.
#Cyan Bike
def cyan_up():
    if cyan_bike.heading() - 270 != 0:
        cyan_bike.setheading(90)
def cyan_down():
    if cyan_bike.heading() != 90 or 0:
        cyan_bike.setheading(-90)
def cyan_right():
    if cyan_bike.heading() != 180:
        cyan_bike.setheading(0)
def cyan_left():
    if cyan_bike.heading() != 0:
        cyan_bike.setheading(180)

#Magenta Bike
def magenta_up():
    if magenta_bike.heading() - 270 == 0:
        pass
    else:
        magenta_bike.setheading(90)
def magenta_down():
    if magenta_bike.heading() == 90 or 0:
        pass
    else:
        magenta_bike.setheading(-90)
def magenta_right():
    if magenta_bike.heading() == 180:
        pass
    else:
        magenta_bike.setheading(0)
def magenta_left():
    if magenta_bike.heading() == 0:
        pass
    else:
        magenta_bike.setheading(180)

#Explosion Particles
explosion_effects = []
def bike_explosion(x,y):
    explosion = turtle.Turtle()
    explosion.pensize(1)
    explosion.hideturtle()
    explosion.penup()
    explosion.setposition(x,y)
    explosion.pendown()
    explosion.color('#FF4500')
    for _ in range(7):
        length = random.randint(10,30)
        if explosion.stamp() in explosion_effects:
            explosion.clearstamps()
        else:
            explosion_effects.append(explosion.stamp())
        explosion.forward(length)
        explosion.backward(length)
        explosion.left(50)
        wn.update()
    time.sleep(1)
    explosion.clear()

def cyan_win(): # Win system for adding points
    #print('Cyan Wins!')
    one.cyan_add_one()
    score.clear()
    score.write(f'Cyan {one.cyan_score}, Magenta {one.magenta_score}',align="center",font=("Courier", 24, "normal"))
def magenta_win():
    #print('Magenta Wins!')
    one.mag_add_one()
    score.clear()
    score.write(f'Cyan {one.cyan_score}, Magenta {one.magenta_score}',align="center",font=("Courier", 24, "normal"))

#Resets ALL Coords and line historys.
def Reset():
    magenta_bike.sety(224)
    magenta_bike.setx(0)
    cyan_bike.sety(-224)
    cyan_bike.setx(0)
    magenta_bike.setheading(-90)
    cyan_bike.setheading(90)
    cyan_bike.clear()
    magenta_bike.clear()
    magenta_history.clear()
    cyan_history.clear()
    wn.update()

def magenta_reset(): # Main reset system for each bike
    bike_explosion(x_cyan,y_cyan)
    magenta_win()
    Reset()
def cyan_reset():
    bike_explosion(x_magenta,y_magenta)
    cyan_win()
    Reset()

#Bike and keyboard listeners.
#Cyan 
wn.onkey(cyan_up,'w')
wn.onkey(cyan_down,'s')
wn.onkey(cyan_right,'d')
wn.onkey(cyan_left,'a')
#Magenta
wn.onkey(magenta_up,'Up')
wn.onkey(magenta_down,'Down')
wn.onkey(magenta_right,'Right')
wn.onkey(magenta_left,'Left')

#Main Game Loop
while True:
    wn.listen()
    wn.update()
    time.sleep(0.1)
    cyan_bike.forward(cyan_bike.speed())
    magenta_bike.forward(magenta_bike.speed())

    #Position Logging
    x_cyan, y_cyan = round(cyan_bike.xcor()), round(cyan_bike.ycor())
    x_magenta, y_magenta = round(magenta_bike.xcor()), round(magenta_bike.ycor())

    #Border Detection/ Border Scoring
    if (x_cyan, y_cyan) in magenta_history or (x_cyan, y_cyan) in cyan_history: #checks if the current cyan coords are in magentas history or cyan's history
        print('Maginta Wins!')
        magenta_reset()
    elif (x_magenta, y_magenta) in cyan_history or (x_magenta, y_magenta) in magenta_history: #checks if the current magenta coords are in cyan's history or magenta's history
        print('Cyan Wins!')
        cyan_reset()
    #Border Control
    elif cyan_bike.xcor() >= 320 or cyan_bike.xcor() <= -320: #Boundry Wall
        print('Out Of Bounds')
        magenta_reset()
    elif cyan_bike.ycor() >= 320 or cyan_bike.ycor() <= -320: #Boundry Wall
        print('Out Of Bounds')
        magenta_reset()
    elif magenta_bike.xcor() >= 320 or magenta_bike.xcor() <= -320: #Boundry Wall
        print('Out Of Bounds')
        cyan_reset()
    elif magenta_bike.ycor() >= 320 or magenta_bike.ycor() <= -320: #Boundry Wall
        print('Out Of Bounds')
        cyan_reset()
    elif (x_cyan,y_cyan) == (x_magenta,y_magenta): #Head on collisions. Ties
        print('Tie')
        bike_explosion(x_magenta,y_magenta)
        Reset()
    else:
        cyan_history.add((x_cyan,y_cyan))
        magenta_history.add((x_magenta,y_magenta))
        #Adding New X/Y Coords To Sets/Historys at the end of the loop.

    #Just some informational logs if you want to see how it works.
    #print(f'Cyan Logging :\n \t{cyan_history}')
    #print(f'Magenta Logging :\n ,\t{magenta_history}')
