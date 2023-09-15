import turtle

def turtle_move(angle):
	turtle.setheading(angle)
	turtle.stamp()
	turtle.forward(50)

def restart():
	turtle.reset()

turtle.shape('turtle')

turtle.onkey(lambda : turtle_move(0), 'd')
turtle.onkey(lambda : turtle_move(0), 'D')
turtle.onkey(lambda : turtle_move(90), 'w')
turtle.onkey(lambda : turtle_move(90), 'W')
turtle.onkey(lambda : turtle_move(180), 'a')
turtle.onkey(lambda : turtle_move(180), 'A')
turtle.onkey(lambda : turtle_move(270), 's')
turtle.onkey(lambda : turtle_move(270), 'S')
turtle.onkey(restart, 'Escape')

turtle.listen()

turtle.exitonclick()
