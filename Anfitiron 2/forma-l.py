import turtle

t = turtle.Turtle()
t.color("black", "limegreen")

t.begin_fill()

t.forward(60)
t.left(90)
t.forward(120)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.right(90)
t.forward(120)
t.left(90)

t.end_fill()

t.hideturtle()
turtle.done()