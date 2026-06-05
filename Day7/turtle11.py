import turtle, random, time
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Maximize window
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta",
          "white", "light blue", "gold", "violet", "light green", "pink"]

for _ in range(100):
    t.penup()
    t.goto(random.randint(-600, 600), random.randint(-350, 350))  # Wider range for full screen
    t.color(random.choice(colors))
    size = random.randint(4, 6)
    t.begin_fill()
    for _ in range(5): t.forward(size); t.right(144)
    t.end_fill()
    time.sleep(0.01)

turtle.done()