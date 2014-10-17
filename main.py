from Tkinter import *
from elevator import *
from floorbutts import *
import time
elevators = []
floorbuttups = []
floorbuttdowns = []
floorbutts = []
simstate = False
speed = 2

class App:
    def __init__(self, master):
        self.w = Canvas(master, width=SW/2, height=SH)
        self.f = Canvas(master, width=SW/2, height=SH)
        self.w.bind("<Button-1>", self.callback)
        self.w.pack(side=LEFT)
        self.f.pack(side=LEFT)
        self.makefloors()
        self.makefbutts()
        self.makelevs()
        self.start = Button(self.f, text="Start Simulation", command=self.sim)
        self.start.pack(side=LEFT)
        self.stop = Button(self.f, text="Stop Simulation", command=self.stop, state=DISABLED)
        self.stop.pack(side=LEFT)

    def callback(self, event):
        if not simstate:
            return
        x, y = event.x, event.y
        if x>=520 and x<=540:
            for i in range(10):
                if y>=30+i*SH/12 and y<=15+(2*i+1)*SH/24:
                    # print x, y, 'up'
                    floorbuttups[i].on = True
                    break
                elif y>=25+(2*i+1)*SH/24 and y<=10+(i+1)*SH/12:
                    # print x, y, 'down'
                    floorbuttdowns[i].on = True
                    break

    def makefloors(self):
        global SW, SH
        for i in range(10):
            self.w.create_rectangle(100, 20+i*SH/12, 200, 20+(i+1)*SH/12, fill="white")
            self.w.create_rectangle(200, 20+i*SH/12, 300, 20+(i+1)*SH/12, fill="white")
            self.w.create_rectangle(300, 20+i*SH/12, 400, 20+(i+1)*SH/12, fill="white")
            self.w.create_rectangle(400, 20+i*SH/12, 500, 20+(i+1)*SH/12, fill="white")

    def makefbutts(self):
        global SW, SH, floorbuttups, floorbuttdowns, floorbutts
        for i in range(10):
            b = Floorbutt(self.w, i, 0, SH)
            floorbuttups.append(b)
            floorbutts.append(b)
            b = Floorbutt(self.w, i, 1, SH)
            floorbuttdowns.append(b)
            floorbutts.append(b)

    def makelevs(self):
        global SW, SH, elevators
        for i in range(4):
            e = Elevator(self.w, i+1, SW, SH)
            elevators.append(e)

    def sim(self):
        global simstate
        simstate = True
        self.start.config(state=DISABLED)
        self.stop.config(state=NORMAL)
        master.after(5, simulate())

    def stop(self):
        global simstate
        simstate = False
        self.start.config(state=NORMAL)
        self.stop.config(state=DISABLED)
        

master = Tk()

posx = 0
posy = 0
SW = master.winfo_screenwidth()
SH = master.winfo_screenheight()
master.wm_geometry("%dx%d+%d+%d" % (SW, SH, posx, posy))

Label(master, text="Elevator Simulation", fg="#05b",font="Purisa 18 bold underline").pack()
app = App(master)

def simulate():
    global SH, elevators, floorbuttdowns, floorbuttups, floorbutts, speed
    
    for b in floorbutts:
        b.update(app.w, SH)
        
        if b.on:
            elevSet = False
            for e in elevators:
                if e.dest==b.floor:
                    elevSet = True
                    break
            if not elevSet:
                for e in elevators:
                    if e.dest==-1:
                        e.dest = b.floor
                        e.butt = b
                        if e.floor<9-b.floor:
                            e.vel = -speed
                        elif e.floor>9-b.floor:
                            e.vel = speed
                        break



    for e in elevators:
        if e.vel!=0:
            e.update(app.w, SH)
    if simstate:
        master.after(5, simulate)

master.mainloop()