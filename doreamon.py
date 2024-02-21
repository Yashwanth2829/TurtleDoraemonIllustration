from turtle import *

# Doraemon with Python Turtle
def move(x, y):
    penup()
    goto(x, y)
    pendown()

def draw_eye():
    fillcolor("#ffffff")
    begin_fill()
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            left(3)
            forward(a)
        else:
            a += 0.05
            left(3)
            forward(a)
    tracer(True)
    end_fill()

def draw_whiskers():
    move(-32, 135)
    seth(165)
    forward(60)

    move(-32, 125)
    seth(180)
    forward(60)

    move(-32, 115)
    seth(193)
    forward(60)

    move(37, 135)
    seth(15)
    forward(60)

    move(37, 125)
    seth(0)
    forward(60)

    move(37, 115)
    seth(-13)
    forward(60)

def draw_mouth():
    move(5, 148)
    seth(270)
    forward(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)

def draw_muffler():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    forward(200)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    forward(207)
    circle(-5, 90)
    forward(10)
    circle(-5, 90)
    end_fill()

def draw_nose():
    move(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()

def draw_black_eye():
    seth(0)
    move(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    move(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    move(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    move(0, 0)

def draw_face():
    forward(183)
    left(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    forward(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    move(63.56, 218.24)
    seth(90)
    draw_eye()
    seth(180)
    penup()
    forward(60)
    pendown()
    seth(90)
    draw_eye()
    penup()
    seth(180)
    forward(64)

def draw_necktie():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()

def draw_Doraemon():
    draw_necktie()
    draw_muffler()
    draw_face()
    draw_nose()
    draw_mouth()
    draw_whiskers()
    move(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    forward(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    forward(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    seth(180)
    forward(70)
    seth(90)
    circle(30, 180)
    seth(180)
    forward(70)

    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    forward(40)

    circle(-30, 230)
    seth(45)
    forward(81)
    seth(0)
    forward(203)
    circle(5, 90)
    forward(10)
    circle(5, 90)
    forward(7)
    seth(40)
    circle(150, 10)
    seth(30)
    forward(40)
    end_fill()

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    move(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    forward(15)
    circle(-15, 180)
    forward(90)
    circle(-15, 180)
    forward(10)
    end_fill()

    move(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    forward(15)
    circle(15, 180)
    forward(90)
    circle(15, 180)
    forward(10)
    end_fill()

    move(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()

    move(-103.42, 15.09)
    seth(0)
    forward(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    move(5, -40)
    seth(0)
    forward(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    forward(70)

    move(-103.42, 15.09)
    forward(90)
    seth(70)
    fillcolor('#ffd200')
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    forward(15)
    dot(10)
    move(0, -150)
    draw_black_eye()

if __name__ == '__main__':
    screensize(800, 600, "#f0f0f0")
    pensize(3)
    speed(9)
    draw_Doraemon()
    move(100, -300)
    write('by yashwanth sai', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()
