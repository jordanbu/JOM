import turtle

t = turtle.Turtle()
t.color("black", "limegreen")

t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(120)
t.end_fill()

t.hideturtle()
turtle.done()