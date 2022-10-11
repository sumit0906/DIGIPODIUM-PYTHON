from turtle import*
def triangle():
        for i in range(3):
            pencolor('red')
            forward(100)
            left(60)
def square():
        for i in range(4):
            pencolor('orange')
            forward(100)
            left(90)

def pentagon():
        for i in range(5):
           pensize(5)
           pencolor('blue')
           forward(100)
           right(72)

shape = input("enter the shape among triangle ,square ,pentagon")
if shape == ('triangle'):
    triangle()
elif shape ==('square'):
    square()

elif shape== ('pentagon'):
    pentagon()

else:
    print("wrong input")

mainloop()