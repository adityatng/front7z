from turtle import*
import random




mt = Turtle()

mt.screen.setup(500,500)
mt.screen.bgcolor('black')
mt.speed(0)
mt.ht()

colors=[
        'blue','red','yellow','orange','purple',
        'magenta','pink','lime','green','gold','silver','violet'
        ]

def draw_fw(t):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    d = random.randint(20,100)

    for i in range(36):
        t.forward(d)
        t.backward(d)
        t.right(10)
for i in range(10):
    draw_fw(mt)

mt.penup()
mt.goto(0,200)
mt.pendown()
mt.color('white')
mt.write('Happy 4th of jully', align='center', font=('verdana',24,'normal'))
