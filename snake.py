import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Snake = 1")

status_label = tk.Label(
    root,
    text="test",
    bd=1,
    padx=1, pady= 1)
status_label.pack()

SIZE = 20
W = 400
H = 400

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

snake = [(10, 10)]

game_over = False

dx = 1
dy = 0

max_x = 20
max_y = 20


food = (random.randint(0, W//SIZE - 1),
            random.randint(0, H//SIZE - 1))

wallset = set()

for _ in range(25):
    wallset.add((random.randint(1, W//SIZE - 2),
                           random.randint(1, H//SIZE - 2)))
# wall = (random.randint(0, W//SIZE - 1),
#             random.randint(0, H//SIZE - 1))
# superfood = (random.randint(0, W//SIZE - 1),
#        random.randint(0, H//SIZE - 1))

def draw():
    
    
    canvas.delete("all")
 
    fx, fy = food
    canvas.create_oval(fx*SIZE, fy*SIZE, fx*SIZE+SIZE, fy*SIZE+SIZE, fill="red")

    # sx, sy = superfood
    # canvas.create_oval(sx*SIZE, sy*SIZE, sx*SIZE+SIZE, sy*SIZE+SIZE, fill="yellow")

    for x, y in wallset:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                x*SIZE+SIZE, y*SIZE+SIZE,
                                fill="black")


    for (x,y) in snake:

        canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE+SIZE, y*SIZE+SIZE, fill="green")


def game_loop():
    
    
    global snake, food, wall, game_over
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    print(new_head[0])

    if new_head in snake:
        print("touching")
        game_over = True
        status_label.config(text="Game Over")
    if new_head[0] < 0 or new_head[0] >= max_x or new_head[1] < 0 or new_head[1] >= max_y:
        print("wall collision")

        game_over = True
        status_label.config(text="Game Over")
    if food in wallset:
        food = (random.randint(0, W//SIZE - 1),
                random.randint(0, H//SIZE - 1))
    
    snake.insert(0, new_head)



    if new_head == food:
        food = (random.randint(0, W//SIZE - 1),
                random.randint(0, H//SIZE - 1))
        snake.insert(0, new_head)
        # for i in range(99):
        #     snake.insert(0, new_head)
        
    
        # 
    
   
        # status_label.config(text="Game Over")
    # if new_head == superfood:
    #     superfood = (random.randint(0, W//SIZE - 1),
    #             random.randint(0, H//SIZE - 1))
    #     for i in range(4):
    #         snake.insert(0, new_head)
    if new_head in wallset:
        game_over = True
        status_label.config(text="Game Over")

    else:
        snake.pop()

    draw()

    

    if game_over == False:
        root.after(150, game_loop)
        print(game_over)

def up(event):
    global dx, dy
    if dx != 0 and dy != 1:
        dx, dy = 0, -1

def down(event):
    global dx, dy
    if dx != 0 and dy != -1:
        dx, dy = 0, 1

def left(event):
    global dx, dy
    if dx != 1 and dy != 0:
        dx, dy = -1,0

def right(event):
    global dx, dy
    if dx != -1 and dy != 0:
        dx, dy = 1, 0

root.bind("<Up>",up)
root.bind("<Down>",down)
root.bind("<Left>",left)
root.bind("<Right>",right)

draw()
root.after(150, game_loop)



root.mainloop()
