import turtle as t
t.bgcolor('black')
t.setup(1537,865)
color=('green','cyan','orange')
t.tracer(500)
t.width(10)
for i in range(8360):
    t.fillcolor('black')
    t.pencolor(color[i%3])
    t.rt(100)
    t.fd(i)
    t.rt(90)
    t.fd(i)
    t.lt(300)
    t.fd(i)
t.done()