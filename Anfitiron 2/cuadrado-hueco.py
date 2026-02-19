import turtle

t = turtle.Turtle()
t.color("black", "limegreen")

# Cuadrado grande
t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# Hueco interno
t.penup()
t.goto(40, 40)
t.pendown()
t.color("white")

t.begin_fill()
for _ in range(4):
    t.forward(70)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()
