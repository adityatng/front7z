#day4/100daysofpython
#PythonTurtle2

from turtle import*

f7z = Turtle()
f7z.screen.bgcolor('black')
speed(1)
ht()
f7z.penup()
f7z.goto(-300,250)
f7z.pendown()

f7z.color('red')
f7z.begin_fill()
f7z.fd(600)
f7z.rt(90)
f7z.fd(167)
f7z.rt(90)

f7z.fd(600)
f7z.rt(90)
f7z.fd(167)
f7z.rt(90)
f7z.end_fill()


f7z.rt(90)
f7z.fd(334)

f7z.color('white')
f7z.begin_fill()
f7z.lt(90)
f7z.fd(600)
f7z.lt(90)
f7z.fd(167)
f7z.lt(90)
f7z.fd(600)
f7z.end_fill()
home()

f7z.bk(300)
f7z.color('black')
f7z.write('INDONESIA', font='Verdana')

exitonclick()