import turtle

turtle.shape('turtle')

#첫번째 사각형
turtle.pensize(3)
turtle.pencolor("red")
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)

#두번째 사각형
turtle.pencolor("orange")
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

#띄우고 이동
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

#세번째 사각형
turtle.pendown()
turtle.pencolor("yellow")
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

#띄우고 이동
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

#네번째 사각형
turtle.pendown()
turtle.pencolor("green")
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)



