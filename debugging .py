##It may be easier to do so if you improve the code quality. 
##copy and paste this code into a new file named “debugging.py”

import turtle # imports the turtle library

yp7 = turtle.clone() #this creates a new turtle and stores it in a variable
t = 200
b = -200

#draw the letter ‘A’

turtle.hideturtle() # this hides the arrow of the turtle called turtle


yp7.pendown()


yp7.goto(0,0)


yp7.penup()

#a,c = yp7.pos()

yp7.goto(t,b)

yp7.pendown()
yp7.goto(t+100, b+300)
yp7.goto(t+200, b)
yp7.goto(t+167,b+100)
yp7.goto(t+34, b+100)


#yp7.goto(a+300, c+100)

turtle.mainloop() # all turtle commands must go before this line!!!

