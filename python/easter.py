from turtle import *

mw = Screen()
mw.bgcolor("wheat")

f7z = Turtle()
f7z.speed("fastest")

def mR(t, posx, posy, x, y, c):
    t.penup()
    t.color(c)
    t.setheading(0)
    t.goto(posx, posy)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.fd(x)
        t.rt(90)
        t.fd(y)
        t.rt(90)
    t.end_fill()
def mC(t, posx, posy, r, c):
    t.penup()
    t.color(c)
    t.setheading(0)
    t.goto(posx, posy)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
def mA(t, posx, posy, r, angel, heading, c):
    t.penup()
    t.color(c)
    t.setheading(heading)
    t.goto(posx, posy)
    t.pendown()
    t.begin_fill()
    t.circle(r,angel)
    t.end_fill()

mR(f7z, -250, 50, 50, 100, "silver")
mC(f7z, -225, 25, 25, "silver")
mR(f7z, -240, 50, 30, 90, "hot pink")
mC(f7z, -225, 35, 15, "hot pink")

mR(f7z, -180, 50, 50, 100, "silver")
mC(f7z, -155, 25, 25, "silver")
mR(f7z, -170, 50, 30, 90, "hot pink")
mC(f7z, -155, 35, 15, "hot pink")

mC(f7z, -190, -220, 100, "silver")
mC(f7z, -190, -500, 150, "silver")
mC(f7z, -190, -450, 100, "hot pink")

mC(f7z, -215, -110, 10, "grey")
mC(f7z, -165, -110, 10, "grey")

f7z.penup()
f7z.goto(-200,-130)
f7z.color("hot pink")
f7z.pendown()
f7z.begin_fill()
f7z.goto(-180,-130)
f7z.goto(-190,-150)
f7z.goto(-200,-130)
f7z.end_fill()

mA(f7z, -190, -150, 20, 150, -90, "hot pink")
mA(f7z, -190, -150, -20, 150, -90, "hot pink")

f7z.penup()
f7z.goto(-200,-20)
f7z.pendown()
f7z.seth(270)
f7z.color('red')
f7z.circle(100,180)

# f7z.penup()
# f7z.goto(100,200)
# f7z.color("navy")
# f7z.pendown()
# f7z.write("Happy", align="center", font = ("Verdana", 110, "bold"))

# f7z.penup()
# f7z.goto(100,90)
# f7z.color("navy")
# f7z.pendown()
# f7z.write("Easter!", align="center", font = ("Verdana", 110, "bold"))

f7z.ht()

exitonclick() 