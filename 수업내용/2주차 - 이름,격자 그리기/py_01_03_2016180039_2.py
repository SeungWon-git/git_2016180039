import turtle as t

def move(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()

a=0
b=0
for i in range(0,5+1):
	move(0,b)
	t.forward(500)
	b=b+100

t.left(90)

for j in range(0,5+1):
	move(a,0)
	t.forward(500)
	a=a+100

t.exitonclick()
