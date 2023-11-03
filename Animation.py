import turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(2)


for i in range(20):
    for colours in ['red','blue','purple','green','pink','cyan','orange','yellow','brown']:
        turtle.color(colours)
        turtle.left(12)
        for i in range(4):
            turtle.forward(200)
            turtle.left(90)




