import turtle

t = turtle.Turtle()
t.color("black", "limegreen")

t.begin_fill()

t.goto(-60, 80)
t.goto(60, 80)
t.goto(-60, -80)
t.goto(60, -80)
t.goto(-60, 80)

t.end_fill()

t.hideturtle()
turtle.done()
