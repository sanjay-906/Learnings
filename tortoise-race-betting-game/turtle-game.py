import turtle
from turtle import Turtle
from random import randint

#creating the objects
a1=Turtle()
a2=Turtle()
a3=Turtle()
a4=Turtle()
a5=Turtle()
a6=Turtle()

#draw track
track= Turtle()
track.penup()
track.goto(-400,216)
track.pendown()
track.goto(400, 216)
track.goto(400, -36)
track.goto(-400, -36)
track.hideturtle()

#textinput
text= Turtle()
text.hideturtle()
text.penup()
text.goto(-120,-180)
text.write("Tortoise Race", font=("Verdana", 27, "normal"))

#start line
sline= Turtle()
sline.hideturtle()
sline.penup()
sline.goto(-300, 216)
sline.pendown()
sline.goto(-300, -36)

#finish line
fline= Turtle()
fline.hideturtle()
fline.penup()
fline.goto(300, 216)
fline.pendown()
fline.goto(300, -36)

#assigning the colors to the object
a1.color('red')
a2.color('orange')
a3.color('purple')
a4.color('green')
a5.color('blue')
a6.color('pink')

#adding shape of the object
a1.shape('turtle')
a2.shape('turtle')
a3.shape('turtle')
a4.shape('turtle')
a5.shape('turtle')
a6.shape('turtle')

#draw routes
a1_path= Turtle()
a1_path.hideturtle()
a1_path.color('red')

a2_path= Turtle()
a2_path.hideturtle()
a2_path.color('orange')

a3_path= Turtle()
a3_path.hideturtle()
a3_path.color('purple')

a4_path= Turtle()
a4_path.hideturtle()
a4_path.color('green')

a5_path= Turtle()
a5_path.hideturtle()
a5_path.color('blue')

a6_path= Turtle()
a6_path.hideturtle()
a6_path.color('pink')


def propogate(a1,a2,a3,a4,a5,a6, draw_path= False):
    a1.penup()
    a1.goto(-300,0)
    a1.pendown()

    a2.penup()
    a2.goto(-300,36)
    a2.pendown()

    a3.penup()
    a3.goto(-300,72)
    a3.pendown()

    a4.penup()
    a4.goto(-300,108)
    a4.pendown()

    a5.penup()
    a5.goto(-300,144)
    a5.pendown()

    a6.penup()
    a6.goto(-300,180)
    a6.pendown()

    if draw_path:
        a1_path.goto(300,0)
        a2_path.goto(300,36)
        a3_path.goto(300,72)
        a4_path.goto(300,108)
        a5_path.goto(300,144)
        a6_path.goto(300,180)

propogate(a1_path, a2_path, a3_path, a4_path,
            a5_path, a6_path, draw_path= True)

def assign_speed(flag= False):
    if flag:
        return 12
    return randint(1,12)

def decide_winner():
    return randint(1,6)

while(True):
    #moving the objects to the starting point of the race
    propogate(a1,a2,a3,a4,a5,a6)

    tortoises= {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0}
    winner= decide_winner()
    for i,key in enumerate(tortoises):
        if(i+1==winner):
            tortoises[key]= assign_speed(True)
        else:
            tortoises[key]= assign_speed()

    #map speeds
    go= {
            "red": tortoises['x1'],
            "orange": tortoises['x2'],
            "purple": tortoises['x3'],
            "green": tortoises['x4'],
            "blue": tortoises['x5'],
            "pink": tortoises['x6']
        }

    #place bet
    choice= input(str("which Tortise will you bet on?(type color):"))

    #starting the race
    for i in range (50):
        a1.forward(go['red'])
        a2.forward(go['orange'])
        a3.forward(go['purple'])
        a4.forward(go['green'])
        a5.forward(go['blue'])
        a6.forward(go['pink'])

    #decide winner
    maxt = max(go['red'],go['orange'],go['purple'],go['green'],go['blue'],go['pink'])
    if go[choice]==maxt:
        print("you won!")
    else:
        print("you lost")
    result=input("Want to continue(y/n):")

    if(result=='y'):
        continue
    elif(result=='n'):
        turtle.bye()
        break
    else:
        print("Invalid")
