import turtle as trtl
import random
miles = trtl.Turtle()



player_bot = trtl.Turtle()
player_bot.pencolor("red")




miles.speed(0)    
wall_width = 10
door_width = 10
distance = 5
# miles.left(90)
miles.ht()

def drawDoor():
    miles.penup()
    miles.forward(door_width)
    miles.pendown()

def drawBarrier():
    miles.right(90)
    miles.forward(wall_width*2)
    miles.backward(wall_width*2)
    miles.left(90)


for i in range(50):
    if i > 4:
        door = random.randint(door_width, distance - 2 * door_width)
        barrier = random.randint(wall_width, distance - 2 * door_width)

        if (door < barrier):
            miles.forward(door)
            drawDoor()
            miles.forward(barrier - door - door_width)
            drawBarrier()
            miles.forward(distance - barrier)
        else:
            miles.forward(barrier)
            drawBarrier()
            miles.forward(door - barrier)
            drawDoor()
            miles.forward(distance - door - door_width)

        miles.left(90)
    distance += wall_width
    
def up():
    player_bot.setheading(90)
    player_bot.forward(5)


def down():
    player_bot.setheading(270)
    player_bot.forward(5)


def left():
    player_bot.setheading(180)
    player_bot.forward(5)


def right():
    player_bot.setheading(0)
    player_bot.forward(5)




wn = trtl.Screen()


wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.listen()
wn.mainloop()
