import turtle
import math
screen = turtle.Screen()
screen.title('Squares Circle - PythonTurtle.Academy')
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def draw_square(x,y,length,direction,color):
    turtle.up()
    turtle.goto(x-length/(2**0.5)*math.cos(math.radians(direction+45)),y-length/(2**0.5)*math.sin(math.radians(direction+45)))
    turtle.seth(direction)
    turtle.color(color)
    turtle.down()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)

def draw_square_circle(radius,direction,n):
    length = 2*radius*math.sin(math.radians(180/n))
    length = length/(2**0.5)
    for _ in range(n):
        draw_square(radius*math.cos(math.radians(180/n))*math.cos(math.radians(direction)),\
                    radius*math.cos(math.radians(180/n))*math.sin(math.radians(direction)),\
                    length, direction+45,'blue')
        direction += 360/n
        
draw_square_circle(600,0,20)