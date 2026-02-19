import turtle

t = turtle.Turtle()
turtle.bgcolor("white")

t.color("black", "limegreen")
t.begin_fill()

for _ in range(8):
    t.forward(80)
    t.left(45)

t.end_fill()
t.hideturtle()
turtle.done()