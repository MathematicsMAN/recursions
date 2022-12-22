from turtle import *


def step(n, steps):
    fd(steps)
    if n == 1: bk(steps)
    else:
        lt(108)
        step(n-1, steps // 2)
        rt(72)
        step(n-1, steps // 2)
        rt(72)
        step(n-1, steps // 2)
        rt(72)
        step(n-1, steps // 2)
        lt(108)
        bk(steps)


# speed(15)   # uncomment this command and comment next command
tracer(0, 0)

lt(90)
step(6, 120)  # change 6 to 8


mainloop()
