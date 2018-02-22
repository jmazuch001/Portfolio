import turtle

def draw_funkyflower(some_turtle):
    for i in range (1,50):
        some_turtle.left(35)
        some_turtle.forward(70)
        some_turtle.right(140)
        some_turtle.forward(70)
        some_turtle.right(90)
        some_turtle.forward(70)
        some_turtle.right(10)
    some_turtle.seth(270)
    some_turtle.forward(300)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange", "blue")
    brad.speed(40)
    draw_funkyflower(brad)

    window.exitonclick()

draw_art()
