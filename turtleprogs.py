import turtle
from turtle import *

def horny_square():
    for trtl in range(4):
        forward(200)
        back(100)
        left(90)
    done()
        
#horny_square()


def flag():
    forward(200)
    for tu in range(2):
        right(120)
        forward(100)
    done()

#flag()


def drawing_letter_Y():
    forward(100)
    left(45)
    forward(100)
    back(100)
    right(90)
    forward(100)
    done()

#drawing_letter_Y()


def Say_Hi():
    forward(200)
    back(100)
    right(90)
    forward(100)
    left(90)
    forward(100)
    back(200)
    right(90)

    penup()
    forward(100)
    left(90)
    pendown()
    forward(200)
    done()

#Say_Hi()


def three_srtings():
    forward(200)

    penup()
    right(90)
    forward(40)
    right(90)

    pendown()
    forward(200)

    penup()
    left(90)
    forward(40)
    left(90)

    pendown()
    forward(200)
    done()

#three_srtings()


def nested_squares():
    turtle.shape("square")
    turtle.fillcolor("white")

    for side in range(100, 0, -10):
        turtle.shapesize(side / 10)
        turtle.stamp()
    done()

#nested_squares()


def steps_stairs():
    for _ in range(10):
        left(90)
        forward(20)
        right(90)
        forward(20)

    exitonclick()

#steps_stairs()


def nested_squares2():
    for shape in range(1, 10 + 1):
        for sides in range(4):
            forward(10 + shape * 5)
            right(90)

        penup()
        left(90)
        forward(10)
        left(90)
        forward(10)
        left(180)
        pendown()

    done()

#nested_squares2()


def chain_squares():
    for shape in range(1, 10 + 1):
        for sides in range(4):
            forward(5 + shape * 5)
            right(90)

        penup()
        left(90)
        forward(10)
        left(90)
        forward(10)
        left(180)
        pendown()
    done()

#chain_squares()


def spider_web():
    speed(100)
    
    for i in range(6):
        forward(150)
        backward(150)
        right(60)

    side = 150
    for i in range(15):
        penup()
        goto(0,0)
        pendown()
        setheading(0)
        forward(side)
        right(120)
        for j in range(6):
            forward(side)
            right(60)
        side = side - 10

    done()

#spider_web()


def Six_Lines():
    for turt in range(6):
        penup()
        right(150)
        forward(200)
        right(150)
        pendown()
        forward(200)

    done()

#Six_Lines()


def Any_Polygon():
    # taking input for the no of the sides of the polygon
    n = int(input("Enter the num of the sides of the polygon: "))

    # taking input for the length of the sides of the polygon
    l = int(input("Enter the length of the sides of the polygon: "))

    for _ in range(n):
        forward(l)
        right(360 / n)

    done()

#Any_Polygon()


def Dodecagon():
    for _ in range(12):
        forward(66)
        right(360 / 12)

    done()

#Dodecagon()

def Diamond():

    speed(1000)

    x = 40
    r = 30
    for j in range(12):
        for i in range(12):
            forward(x)
            right(r)
        right(r)

    done()

#Diamond()

def bactery():

    speed(100)

    x = 20 
    r1 = 30
    r2 = 60
    l = 90

    for i in range(12):
        right(r1)
        forward(x)
        right(r2)
        forward(x)
        right(r2)
        forward(x)
        right(r2)
        forward(x)
        left(l-30)
        forward(x)
        left(l-30)
        forward(x)
        left(l-30)
        forward(x)
        left(l-30)
        forward(x)

    done()

#bactery()


def ZIP():
    for s in range(5):
        x = 20
        y = 30
        for i in range(3):
            right(y)
            forward(x)
            right(y)
        right(y)
        for j in range(4):
            forward(x)
            right(-y)
            right(-y)
        forward(x)
        right(y)

    done()

#ZIP()

'''
def triangles(length):
    for i in range(3):
        forward(length)
        right(120)


penup()
forward(20)
pendown()
triangles(60)

penup()
right(90)
forward(70)
right(90)

#for _ in range(5):
pendown()
triangles(60)

penup()
left(180)
forward(60)
left(60)

pendown()
triangles(60)

done()
'''

'''
def seven_triangles(l):
    for i in range(3):
        forward(l)
        right(120)

penup()
forward(20)
pendown()
seven_triangles(60)

#for _ in range(2):
penup()
right(90)
forward(70)
right(90)

pendown()
seven_triangles(60)

for _ in range(2):
    penup()
    left(180)
    forward(60)
    left(60)

    pendown()
    seven_triangles(60)
    
    penup()
    right(90)
    forward(70)
    right(90)

    pendown()
    seven_triangles(60)

done()
'''

'''
def jeweesh_star(st):
    for i in range(3):
        forward(st)
        right(120)

penup()
right(60)
forward(120)
left(60)
    
pendown()
triangle(60)

penup()
left(30)
forward(35)
right(90)

pendown()
triangle(60)

done()
'''

'''
def six_triangles(length):
    for i in range(3):
        forward(length)
        right(120)

penup()
forward(20)
pendown()
six_triangles(60)

penup()
right(90)
forward(70)
right(90)

pendown()
six_triangles(60)

penup()
left(180)
forward(60)
left(60)

pendown()
six_triangles(60)

penup()
right(90)
forward(70)
right(90)

pendown()
six_triangles(60)

penup()
right(60)
forward(120)
left(60)
    
pendown()
six_triangles(60)

penup()
left(30)
forward(70)
left(150)

pendown()
six_triangles(60)

done()
'''

