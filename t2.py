from turtle import*

pencolor('red')
speed('slowest')
#pentagon
side=5
for i in range(side):
    pensize(1)
    fd(100)
    lt(360/side)
    dot(side*5)
    pensize(5)
    #pencolor('red')
    circle(side*10)

mainloop()   