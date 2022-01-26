import turtle as t
import colorsys as c
h=0.0
t.width(9)
t.setup(1537,865)
t.tracer(10)
t.bgcolor('black')
for i in range(56329):
    color=c.hsv_to_rgb(h,1,1)
    h+=0.009
    t.pencolor('cyan')
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.fd(i)
    t.rt(123)
    t.end_fill()
t.done