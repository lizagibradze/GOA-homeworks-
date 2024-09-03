from turtle import *


#we want to paint a house

#step1 draw swquare 

shape("arrow")

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 180)
pendown()

color("blue")
begin_fill()
left(120)
forward(70)
right(90)
forward(30)
right(90)
forward(65)
right(90)
forward(30)
end_fill()
exitonclick()