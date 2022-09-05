from turtle import Screen
import time

def exit():
    global running
    running = False

print("Deleting system in 10")
time.sleep(1)
for i in range(9, 0, -1):
    print(i)
    time.sleep(1)

running = True

while running:
    win = Screen()
    screenTk = win.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", True)
    win.bgcolor("#000")
    time.sleep(1.5)
    win.bgpic("Bsodwindows10.png")
    win.listen()
    win.onkey(exit, 'p')