#day3/100daysofpython
#PythonTurtle

from turtle import*

f7z = Turtle()
f7z.screen.bgcolor("black")

f7z.pensize(7)
f7z.pencolor("blue")

#F
f7z.penup()
f7z.setpos(-50,50)
f7z.pendown()

f7z.fd(100)
f7z.bk(100)
f7z.rt(90)
f7z.fd(100)

f7z.lt(90)
f7z.fd(100)
f7z.bk(100)

f7z.rt(90)
f7z.fd(100)

#f7
f7z.penup()
f7z.setpos(-50, 50)
f7z.pendown()

f7z.fd(100)
f7z.lt(135)
f7z.fd(141)
f7z.setpos(-50,50)

exitonclick()

