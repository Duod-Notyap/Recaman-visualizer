import time
from turtle import *
import math
placesBeen=[1]
i = 0
c = 0
t = Turtle()
t.pu()
t.setpos(-955, 0)
t.pd()
t.seth(90)
t.speed(0)
def drawSemi(r, l, n):
    k = l-r
    m=2.3
    if(n>0 and k>0):
        for f in range(0, 180):
            t.forward((math.pi*math.fabs(k))*m/360)
            t.right(1)
    elif(n<0 and k>0):
        for f in range(0, 180):
            t.forward((math.pi*math.fabs(k))*m/360)
            t.left(1)
    elif(n>0 and k<0):
        for f in range(0, 180):
            t.forward((math.pi*math.fabs(k))*m/360)
            t.left(1)
    elif(n<0 and k<0):
        for f in range(0, 180):
            t.forward((math.pi*math.fabs(k))*m/360)
            t.right(1)
while True:
    i += 1
    if c-i in placesBeen or c-i <= 0:
        c = c+i
        print("Forward {}".format(c))
        placesBeen.append(c)
        drawSemi(c-i, c, (-1)**(i+1))
    else:
        c = c-i
        print("Back {}".format(c))
        placesBeen.append(c)
        drawSemi(c+i, c, (-1)**(i+1))
