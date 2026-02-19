import turtle

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Casa Cuadrada con Turtle")

# Crear la tortuga
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# -------------------------
# Dibujar la base de la casa (cuadrado)
# -------------------------
t.penup()
t.goto(-100, -100)
t.pendown()

t.fillcolor("#F4A261")  # Color de la casa
t.begin_fill()

for _ in range(4):
    t.forward(200)
    t.left(90)

t.end_fill()

# -------------------------
# Dibujar el techo
# -------------------------
t.goto(-100, 100)
t.fillcolor("#E63946")  # Color del techo
t.begin_fill()

t.goto(0, 180)
t.goto(100, 100)
t.goto(-100, 100)

t.end_fill()

# -------------------------
# Dibujar la puerta
# -------------------------
t.penup()
t.goto(-20, -100)
t.pendown()

t.fillcolor("#6D4C41")
t.begin_fill()

for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.left(90)

t.end_fill()

# -------------------------
# Dibujar ventana izquierda
# -------------------------
t.penup()
t.goto(-70, 0)
t.pendown()

t.fillcolor("#90CAF9")
t.begin_fill()

for _ in range(4):
    t.forward(40)
    t.left(90)

t.end_fill()

# -------------------------
# Dibujar ventana derecha
# -------------------------
t.penup()
t.goto(30, 0)
t.pendown()

t.begin_fill()

for _ in range(4):
    t.forward(40)
    t.left(90)

t.end_fill()

# Ocultar tortuga y finalizar
t.hideturtle()
turtle.done()