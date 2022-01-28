from tkinter import *
from time import sleep

tk = Tk()
title = Text(tk,width=27,height=1)
title.pack()
title.insert(END,"TTP: a Text-Told Platformer")
game = Text(tk,width=27,height=15)
game.pack()
info = Text(tk,width=27,height=2)
info.pack()
tk.update()

levels = {
    0:{
        "layout":[
            "MMMMMMMMM",
            "M       M",
            "M      FM",
            "MMMMMMMMM",
            "         ",
            "Level 1  ",
            ],
        "spawn":[1,2],
        "goal":[7,2],
        "info":"Left/right or a/d to move"
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
        "spawn":[1,3],
        "goal":[8,3],
        "info":"Level Complete!"
        },
    2:{
        "layout":[
            "MMMMMMMMMMMMMMMMMMMMM",
            "M                   M",
            "M                   M",
            "                    F",
            "MM            MM  MMM",
            "M M       MMM       M",
            "M  MMM MM       MM  M",
            "MjijijijijijijijijijM",
            "MMMMMMMMMMMMMMMMMMMMM",
            "                     ",
            "Level 2              "
            ],
        "spawn":[1,3],
        "goal":[20,3],
        "info":"Use space/up to jump"
        },
    3:{
        "layout":[
            "MMMMMMMMMMMMMMMMMM",
            "M                M",
            "M                M",
            "M                M",
            "MM        M   Λ FM",
            "M   Λ   M   MMMMMM",
            "M MMMMM          M",
            "M                M",
            "MijijijijijijijijM",
            "MMMMMMMMMMMMMMMMMM",
            "                  ",
            "Level 3           "
            ],
        "spawn":[1,3],
        "goal":[16,4],
        "info":"Level Complete!\nBeware the spikes!"
        },
    4:{
        "layout":[
            "MMMMMMMMMMMMMMMMMM",
            "M                M",
            "M         M      M",
            "M        M  Λ    M",
            "MM    Λ M  MMMM  M",
            "M    MM         FM",
            "M  Λ            MM",
            "M MMM            M",
            "MijijijijijijijijM",
            "MMMMMMMMMMMMMMMMMM",
            "                  ",
            "Level 4           "
            ],
        "spawn":[1,1],
        "goal":[16,4],
        "info":"Level Complete!"
        }
    }

level = 0
coords = levels[level]["spawn"]
truey = coords[1]
vy = 0

def pixrel(x,y):
    return levels[level]["layout"][coords[1]-y][coords[0]-x]

def xpos():
    return coords[0]

def ypos():
    return coords[1]

def right(event):
    global coords
    if not pixrel(-1,0) == "M":
        coords[0] += 1

def left(event):
    global coords
    if not pixrel(1,0) == "M" and xpos() > 1:
        coords[0] -= 1

def jump(event):
    global vy
    if pixrel(0,-1) == "M":
        vy -= 0.025

def levelinfo():
	info.delete("1.0",END)
	info.insert(END,levels[level]["info"])

game.bind_all("<KeyPress-Right>",right)
game.bind_all("<KeyPress-d>",right)
game.bind_all("<KeyPress-Left>",left)
game.bind_all("<KeyPress-a>",left)
game.bind_all("<KeyPress-Up>",jump)
game.bind_all("<KeyPress-space>",jump)

levelinfo()

while True:
    if coords == levels[level]["goal"]:
        level += 1
        truey = levels[level]["spawn"][1]
        coords = levels[level]["spawn"]
        levelinfo()
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
        title.insert(END,"Game Over! You fell in lava")
        tk.update()
        sleep(1)
        break
    elif pixrel(0,0) == "Λ":
        title.delete("1.0",END)
        title.insert(END,"Game Over! You were spiked!")
        tk.update()
        sleep(1)
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
