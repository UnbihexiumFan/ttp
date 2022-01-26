from time import *

print("TTP: a Text-Told Platformer")

levels = {
    0:{
        "layout":[
            "MMMMMMMMM",
            "M       M",
            "M      FM",
            "MMMMMMMMM"
            ],
        "spawn":[1,3],
        "goal":[7,3]
        }
    }

level = 0
while True:
    leveltext = ""
    for line in levels[level]["layout"]:
        leveltext += line+"\n"
    print("\n"*24+leveltext)
    sleep(0.01)