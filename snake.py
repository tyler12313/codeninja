import tkinter as tk
import random
root = tk.Tk()
root.title("Snake = 1")

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

# superfood = (random.randint(0, W//SIZE - 1),
#        random.randint(0, H//SIZE - 1))

def draw():
    canvas.delete("all")

    fx, fy = food
    canvas.create_oval(fx*SIZE, fy*SIZE, fx*SIZE+SIZE, fy*SIZE+SIZE, fill="red")

    # sx, sy = superfood
    # canvas.create_oval(sx*SIZE, sy*SIZE, sx*SIZE+SIZE, sy*SIZE+SIZE, fill="yellow")

    for (x,y) in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE, x*SIZE+SIZE, y*SIZE+SIZE, fill="green")

def game_loop():
    game_over = False
    if game_over:
        return
    global snake, food, superfood
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    print(new_head[0])

    if new_head in snake:
        print("touching")
        game_over = True

    if new_head[0] < 0 or new_head[0] >= max_x or new_head[1] < 0 or new_head[1] >= max_y:
        print("wall collision")

        game_over = True

    snake.insert(0, new_head)



    if new_head == food:
        food = (random.randint(0, W//SIZE - 1),
                random.randint(0, H//SIZE - 1))
        
    
        # status_label.config(text="Game Over")
    
   
        # status_label.config(text="Game Over")
    # if new_head == superfood:
    #     superfood = (random.randint(0, W//SIZE - 1),
    #             random.randint(0, H//SIZE - 1))
    #     for i in range(4):
    #         snake.insert(0, new_head)
    else:
        snake.pop()

    draw()
    root.after(150, game_loop)

def up(event):
    global dx, dy
    dx, dy = 0, -1

def down(event):
    global dx, dy
    dx, dy = 0, 1

def left(event):
    global dx, dy
    dx, dy = -1,0

def right(event):
    global dx, dy
    dx, dy = 1, 0

root.bind("<Up>",up)
root.bind("<Down>",down)
root.bind("<Left>",left)
root.bind("<Right>",right)

draw()
root.after(150, game_loop)
root.mainloop()
