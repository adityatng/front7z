
from turtle import*

f7z = Turtle()
"""
### Moving the Turtle
#forward=fd(0)
#backward=bk(0)
#right=rt(0)
#left=lt(0)
#penup()
#pendown
#setpos(0,0)
#goto(0,0)
#home()
### Drawing preset figures
#cirle(0)
#dot(0)
### Customize
#bgcolor(str) Screen Color
#title(str) Screen Title
#shapesize(0,0,0) Turtle Size
#pensize(0) Pen Size
#fillcolor(str) Turtle Color
#pencolor(str) Pen Color
#color(str,str)
### Filling in an Image
#begin_fill()
#end_fill()
### Turtle Shape
#shape(str) | square, arrow, circle, turrle, triangle, classic
### Pen Speed
#speed(0)
#undo() if you want to undo your lasst three commands
#clear() Clearing the Screen
#reset() Resetting the Environment
### Leaving a Stamp
#stamp()
#clearstamp(0)
### Cloning Your Turtle
#clone()

### Using Loops and Conditional Statements
f7z.fd(100)
f7z.rt(90)
f7z.fd(100)
f7z.rt(90)
f7z.fd(100)
f7z.rt(90)
f7z.fd(100)
f7z.rt(90)

#For Loops
for i in range(4):
    f7z.fd(100)
    f7z.rt(90)

#While Loops
z=10
while z <=40:
    f7z.circle(z)
    z = z+10
#Conditional Statements

f = input("type  y/n: ")
if f == "y":
    f7z.circle(50)
elif f == "n":
    print("okay")
else:    
    print("invalid reply")


exitonclick()

Turtle methods
Turtle motion
Move and draw
forward() | fd()
backward() | bk() | back()
right() | rt()
left() | lt()
goto() | setpos() | setposition()
setx()
sety()
setheading() | seth()
home()
circle()
dot()
stamp()
clearstamp()
clearstamps()
undo()
speed()
Tell Turtle’s state
position() | pos()
towards()
xcor()
ycor()
heading()
distance()
Setting and measurement
degrees()
radians()
Pen control
Drawing state
pendown() | pd() | down()
penup() | pu() | up()
pensize() | width()
pen()
isdown()
Color control
color()
pencolor()
fillcolor()
Filling
filling()
begin_fill()
end_fill()
More drawing control
reset()
clear()
write()
Turtle state
Visibility
showturtle() | st()
hideturtle() | ht()
isvisible()
Appearance
shape()
resizemode()
shapesize() | turtlesize()
shearfactor()
settiltangle()
tiltangle()
tilt()
shapetransform()
get_shapepoly()
Using events
onclick()
onrelease()
ondrag()
Special Turtle methods
begin_poly()
end_poly()
get_poly()
clone()
getturtle() | getpen()
getscreen()
setundobuffer()
undobufferentries()
Methods of TurtleScreen/Screen
Window control
bgcolor()
bgpic()
clearscreen()
resetscreen()
screensize()
setworldcoordinates()
Animation control
delay()
tracer()
update()
Using screen events
listen()
onkey() | onkeyrelease()
onkeypress()
onclick() | onscreenclick()
ontimer()
mainloop() | done()
Settings and special methods
mode()
colormode()
getcanvas()
getshapes()
register_shape() | addshape()
turtles()
window_height()
window_width()
Input methods
textinput()
numinput()
Methods specific to Screen
bye()
exitonclick()
setup()
title()

"""

from turtle import*

f7z = Turtle()

f7z.width(3)
###left
f7z.penup()
f7z.goto(-300,50)
f7z.pendown()

f7z.rt(160)
f7z.bk(160)

f7z.rt(50)
f7z.bk(60)


f7z.color('black')
f7z.begin_fill()
f7z.rt(110)
f7z.fd(100)

f7z.rt(40)
f7z.bk(60)

f7z.lt(30)
f7z.bk(15)
f7z.lt(30)
f7z.fd(15)
f7z.lt(120)
f7z.fd(10)
f7z.rt(90)
f7z.fd(5)
f7z.rt(90)
f7z.fd(10)

f7z.lt(120)
f7z.fd(15)
f7z.rt(150)
f7z.fd(30)

f7z.rt(150)
f7z.bk(70)

f7z.lt(40)
f7z.fd(60)

f7z.lt(110)
f7z.fd(68)
f7z.lt(55)
f7z.bk(68)
f7z.rt(55)
f7z.bk(60)
f7z.end_fill()










####################################################3

# day9/100daysofpython
# 1

from bs4 import BeautifulSoup

dokumen = \
'''
<html>
<head>
<title>Tutorial BeautifulSoup</title>
</head>

<body>
<p class="judul">Judul Dokumen</p>

<p class="paragraf">Ini adalah contoh paragraf</p>

<a href="https://ngodingdata.com" class="url">Ngodingdata</a>
</body>

</html>
'''

html_soup = BeautifulSoup(dokumen, 'html.parser')

# judul = html_soup.find('p')
# judul = html_soup.find('p', class_='judul')
# judul = html_soup.find('p', class_='judul').text

judul = html_soup.find_all('p')
print judul

# 2

from bs4 import BeautifulSoup
import requests

page = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

# print(page.status_code)
# print(page.content)

quote = soup.find('span', class_='text').text
author = soup.find('small', class_='author').text
tags = [tag.text for tag in soup.find('div', class_='tags').find_all('a'
    , class_='tag')]

print quote
print author
print tags

# 3

from bs4 import BeautifulSoup
import requests

page = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for q in quotes:
    quote = q.find('span', class_='text').text
    author = q.find('small', class_='author').text
    tags = [tag.text for tag in q.find('div', class_='tags'
        ).find_all('a', class_='tag')]

    print quote
    print author
    print tags

# 4

from bs4 import BeautifulSoup
import requests

# quotes di halaman 1 - 10

for page in range(1, 11):

    if page == 1:
        url = 'http://quotes.toscrape.com'
    else:
        url = 'http://quotes.toscrape.com/page/' + str(page)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        print url

        quotes = soup.find_all('div', class_='quote')

        for q in quotes:
            quote = q.find('span', class_='text').text
            author = q.find('small', class_='author').text
            tags = [tag.text for tag in q.find('div', class_='tags'
                ).find_all('a', class_='tag')]

            print quote
            print author
            print tags

#5
from bs4 import BeautifulSoup
import requests
import pandas as pd

data = []

# quotes di halaman 1 - 10
for page in range(1,11):

    if page == 1: 
        url = "http://quotes.toscrape.com"
    else: 
        url = "http://quotes.toscrape.com/page/"+str(page)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')


        quotes = soup.find_all('div', class_='quote')

        for q in quotes:
            quote = q.find('span', class_='text').text
            author = q.find('small', class_='author').text
            tags = [tag.text for tag in q.find('div', class_='tags').find_all('a', class_='tag')]

            data.append({
                'quote': quote,
                'author': author,
                'tags': tags
                })
            df = pd.DataFrame(data)
            df.to_csv('all_quotes.csv', index=False, encoding="utf-8")

###############################################