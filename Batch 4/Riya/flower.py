from turtle import *
def fleur():
    for i in range(300):
        speed(40)
        color('red')
        pensize(2)
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(151)
    
fleur()
mainloop()