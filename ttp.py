from tkinter import *
from time import sleep

tk = Tk()
title = Text(tk,width=27,height=1)
title.pack()
title.insert(END,"TTP: a Text-Told Platformer")
game = Text(tk,width=27,height=15)
game.pack()
tk.update()

levels = {
    0:{
        "layout":[
            "MMMMMMMMM",
            "M       M",
            "M      FM",
            "MMMMMMMMM",
            "         ",
            "Level 1  "
            ],
        "spawn":[1,2],
        "goal":[7,2]
        },
    1:{
        "layout":[
            "MMMMMMMMM",
            "M       M",
            "M       M",
            "M        ",
            "MMMMMMMMM",
            "         ",
            "Level 2  "
            ],
        "spawn":[1,4],
        "goal":[8,3]
        },
    2:{
        "layout":[
            "MMMMMMMMMMMMMMMMMMMMM",
            "M                   M",
            "M                   M",
            "M                M  F",
            "MM            MM  MMM",
            "M M       MMM       M",
            "M  MM  MM           M",
            "MjijijijijijijijijijM",
            "MMMMMMMMMMMMMMMMMMMMM",
            "         ",
            "Level 2  "
            ],
        "spawn":[1,4],
        "goal":[20,3]
        }
    }

level = 0
coords = levels[level]["spawn"]
truey = coords[1]
vy = 0

def pixrel(x,y):
    return levels[level]["layout"][coords[1]-y][coords[0]-x]

def right(event):
    global coords
    if not pixrel(-1,0) == "M":
        coords[0] += 1

def left(event):
    global coords
    if not pixrel(1,0) == "M":
        coords[0] -= 1

def jump(event):
    global vy
    if pixrel(0,-1) == "M":
        vy -= 0.025

game.bind_all("<KeyPress-Right>",right)
game.bind_all("<KeyPress-Left>",left)
game.bind_all("<KeyPress-Up>",jump)
game.bind_all("<KeyPress-space>",jump)

while True:
    if coords == levels[level]["goal"]:
        level += 1
        coords = levels[level]["spawn"]
    vy += 0.0002
    if vy > 0.3:
        vy = 0.3
    if vy < -0.3:
        vy = -0.3
    if pixrel(0,1) == "M" and vy < 0:
        vy = 0
    elif pixrel(0,-1) == "M" and vy > 0:
        vy = 0
    if pixrel(0,-1) in ["i","j"]:
        title.delete("1.0",END)
        title.insert(END,"Game Over!")
        tk.update()
        break
    truey += vy
    coords[1] = round(truey)
    leveltext = ""
    linenum = 0
    for line in levels[level]["layout"]:
        line_ = line
        if coords[1] == linenum:
            line_ = line[:coords[0]]+"O"+line[coords[0]+1:]
        leveltext += line_+"\n"
        linenum += 1
    game.delete("1.0",END)
    game.insert(END,leveltext)
    tk.update()
