import turtle

t = turtle.Turtle()
t.color("black", "limegreen")

t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()