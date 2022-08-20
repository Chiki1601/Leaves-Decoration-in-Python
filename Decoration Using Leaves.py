# leaves decoration in Python turtle

import turtle as t
t.speed(0)
def go_to_pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def Leaf(x):
    t.width(1)
    t.fd(18)
    t.rt(135)
    t.begin_fill()
    t.color("black")
    t.fillcolor("green")
    t.circle(x*2/3,180)
    t.fd(x)
    t.lt(74)
    t.fd(x)
    t.circle(x*2/3,180)
    t.end_fill()
    t.lt(61)
    t.width(0.1)
    t.fd(x)
    t.color("#bfff00")
    for i in range(4):
        t.backward(x/4)
        t.width(2/(4-i))
        t.lt(45)
        t.fd(x/(4-i))
        t.backward(x/(4-i))
        t.rt(90)
        t.fd(x/(4-i))
        t.backward(x/(4-i))
        t.lt(45)
    t.width(2)
    t.color("#4d1919")
    t.backward(18)
    
def Branches():
    for b in range(6):
        t.width(10)
        t.color("black")
        init_pos = t.pos()
        t.seth(-90)
        n = 30
        for i in range(n):
            angle = 45 if i%2 else -45
            t.fd(30-(i*0.8))
            t.rt(angle)
            Leaf(25-(i*0.8))
            t.lt(angle)
        Leaf(5)
        next_pos = init_pos +(-95,0)
        go_to_pos(next_pos[0],next_pos[1])
go_to_pos(-270,280)
t.seth(0)
t.width(20)
t.fd(500)
Branches()

t.done()
