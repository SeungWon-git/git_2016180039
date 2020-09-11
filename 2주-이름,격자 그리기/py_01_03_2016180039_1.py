import turtle as t

t.speed(5)

def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.setheading(0)

def draw_o(x,y):
    move_to(x, y)
    t.circle(40)

def draw_uh(x,y):
    move_to(x-30, y-50)   
    t.forward(30)
    move_to(x, y)
    t.right(90)
    t.forward(100)
    

# (정)

# ㅈ
move_to(-250,65)
t.forward(35)
move_to(-250,65)
t.right(60)
t.forward(55)
move_to(-250,65)
t.right(60+60)
t.forward(55)
move_to(-250,65)
t.right(60+60+60)
t.forward(55)

# ㅓ
draw_uh(-150,90)

# o
draw_o(-185,-100)

# (승)

# ㅅ
move_to(0,100)
t.right(45)
t.forward(60)
move_to(0,100)
t.right(45+90)
t.forward(60)

# ㅡ
move_to(-50,0)
t.forward(100)

# ㅇ
draw_o(0,-100)

# (원)

# ㅇ
draw_o(170,35)

# ㅜ
move_to(180,15)
t.forward(30)
move_to(180,15)
t.right(120)
t.forward(60)
move_to(180,15)
t.right(180)
t.forward(50)

#ㅓ
draw_uh(240,50)

# ㄴ
move_to(160,-35)
t.right(90)
t.forward(60)
t.left(90)
t.forward(100)


t.exitonclick()
