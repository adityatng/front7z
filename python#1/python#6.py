#day6/100daysofpython
#PythonTurtle#4

from turtle import*

f7z = Turtle()

r = 90
l = 60

f7z.screen.bgcolor('#2D3E50')
f7z.color('#FFFFFF')
#lingkaran

f7z.width(12)
f7z.pu()
f7z.setpos(0,-200)
f7z.pd()

f7z.circle(200)

#T
f7z.width(3)
f7z.pu()
f7z.setpos(0,120)
f7z.pd()

f7z.begin_fill()
f7z.fd(120)
f7z.rt(r)
f7z.fd(15)
f7z.rt(r)
f7z.fd(110)
f7z.lt(r)

f7z.fd(l)
f7z.rt(l)
f7z.fd(20)
f7z.rt(120)
f7z.fd(70)
f7z.lt(r)
f7z.fd(110)
f7z.rt(r)
f7z.fd(15)
f7z.rt(r)
f7z.fd(120)
f7z.end_fill()

f7z.pu()
f7z.setpos(0,-130)
f7z.pd()

f7z.begin_fill()
f7z.fd(68)
f7z.lt(r)
f7z.fd(15)
f7z.lt(r)
f7z.fd(l)
f7z.rt(r)
f7z.fd(25)
f7z.lt(l)
f7z.fd(20)
f7z.lt(120)
f7z.fd(35)

f7z.rt(r)
f7z.fd(l)
f7z.lt(r)
f7z.fd(15)
f7z.lt(r)
f7z.fd(68)
f7z.end_fill()

done()