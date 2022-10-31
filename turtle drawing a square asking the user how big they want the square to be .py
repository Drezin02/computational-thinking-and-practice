import turtle
# draw a square

def drawside(lengthofside):
    """this function draws a shape of a square"""
    turtle.forward(lengthofside)
    turtle.right(90)
  #return the area of the square
    return lengthofside*lengthofside

def drawsquare(lengthofside):
    for i in range(4) :
        drawside(lengthofside)
    return lengthofside*lengthofside



lengthofside = int(input("please enter the length of the sides of the square: "))
area = drawsquare(lengthofside)
print ("the area of the square is= "+str(area))
#exit on click and imput cant coexist
turtle.exitonclick()
