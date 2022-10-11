from turtle import*
pencolor('red')
pensize(5)
i=1
while True:
    fd(10+i)
    left(360/6)
    i+=2
    write(i)
    if i>500:
        break

mainloop()