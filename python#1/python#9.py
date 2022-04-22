from turtle import*

f7z = Turtle()

f7z.screen.bgcolor('black')
f7z.speed(0)
f7z.hideturtle()

for i in range(260):
    f7z.color('red')
    f7z.circle(i)
    f7z.color('white')
    f7z.circle(i*0.8)
    f7z.color('white')
    f7z.circle(i*0.6)
    f7z.color('red')
    f7z.circle(i*0.4)
    f7z.right(26)
    f7z.forward(3)

exitonclick()