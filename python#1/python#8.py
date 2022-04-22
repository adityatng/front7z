#day8/100daysofpython

from turtle import*

f7z = Turtle()
f7z.screen.bgcolor('black')
f7z.ht()

f7z.pu()
f7z.goto(-300,250)
f7z.pd()
f7z.color('red')
f7z.rt(90)
for i in range(2):
    f7z.begin_fill()
    f7z.fd(167)
    f7z.lt(90)
    f7z.fd(600)
    f7z.lt(90)
    f7z.end_fill()


f7z.pu()
f7z.goto(-300,83)
f7z.pd()
f7z.color('white')
for i in range(2):
    f7z.begin_fill()
    f7z.fd(167)
    f7z.lt(90)
    f7z.fd(600)
    f7z.lt(90)
    f7z.end_fill()

exitonclick()