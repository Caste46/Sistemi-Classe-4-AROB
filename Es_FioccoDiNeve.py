import turtle 

snow = turtle.Turtle()

finestra = turtle.Screen()

f = open("./Istruzioni.txt", "w")

for k in range(13):
    snow.forward(100)
    f.write("forward:" + str(100) + "\n")
    snow.goto(0,0)
    f.write("goto:(0,0)\n")
    snow.forward(60)
    f.write("forward:" + str(60) + "\n")
    snow.left(30)
    f.write("left:" + str(30) + "\n")
    snow.forward(10)
    f.write("forward:" + str(10) + "\n")
    snow.right(180)
    f.write("right:" + str(180) + "\n")
    snow.forward(10)
    f.write("forward:" + str(10) + "\n")
    snow.right(60)
    f.write("right:" + str(60) + "\n")
    snow.forward(10)
    f.write("forward:" + str(10) + "\n")
    snow.right(180)
    f.write("right:" + str(180) + "\n")
    snow.forward(10)
    f.write("forward:" + str(10) + "\n")
    snow.speed(0)
    f.write("speed:" + str(0) + "\n")

f.close()
finestra.exitonclick()