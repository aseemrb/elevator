#!/usr/bin/env python
# -*- coding: utf-8 -*-#

from Tkinter import *
from elevator import *
from floor import *
from panel import *
import time
elevators = []
floors = []
panels = []
simstate = False
# speed = 1

def simulate():
    global SH, elevators, floors, speed
    for f in floors:
        if f.number<9:
            f.upb.update(app.w, SH)
        if f.number>0:
            f.dwb.update(app.w, SH)

        elev1 = None
        elev2 = None
        
        """Up button found on"""
        if (f.number<9 and f.upb.on) or (f.number==9 and f.dwb.on):
            elevSet = False

            # Elevator standing on the current floor
            for e in elevators:
                if (f.number in e.dest) or e.floor.number==f.number:
                    if e.floor.number==f.number and e.state!='moving':
                        f.upb.on = False
                        if e.state!='opening' and e.state!='opened':
                            e.state = 'opening'
                    elevSet = True
                    break

    
            if not elevSet:
    
                # Nearest elevator below (moving up or stationary) = elev1
                for i in range(f.number-1, -1, -1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if e.direc=='up' or e.direc=='':
                                elev1 = e
                                elevSet = True
                                if e.state=='closed':
                                    break
                        if elev1!=None:
                            break

                # Nearest stationary elevator above
                for i in range(f.number+1, 10, 1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if e.direc=='':
                                elev2 = e
                                elevSet = True
                                break
                        if elevSet:
                            break

                dist1 = 10
                dist2 = 10

                # Compare which is closer
                if elev1!=None:
                    dist1 = abs(elev1.floor.number - f.number)
                if elev2!=None:
                    dist2 = abs(elev2.floor.number - f.number)

                # The elevator below is closer
                if dist1<=dist2 and elev1!=None:
                    elev1.dest.append(f.number)
                    elev1.direc = 'up'

                # The elevator above is closer
                elif dist2<dist1 and elev2!=None:
                    elev2.dest.append(f.number)
                    elev2.direc = 'down'

                # No optimal elevators found
                if elev1==None and elev2==None:
                    mindist = 10
                    for i in range(0, 10, 1):
                        if len(floors[i].elevs)>0:
                            e = floors[i].elevs[0]
                            if abs(e.floor.number-f.number) < mindist:
                                mindist = abs(e.floor.number-f.number)
                                elev1 = e
                    # elev1 is now the most available elevator somehow
                    elev1.dest.append(f.number)
                    if elev1.direc=='' and elev1.state!='closed' and elev1.state!='closing':
                        elev1.state = 'closing'


        """Down button found on"""
        if (f.number>0 and f.dwb.on) or (f.number==0 and f.upb.on):
            elevSet = False

            # Elevator standing on the current floor
            for e in elevators:
                if (f.number in e.dest) or e.floor.number==f.number:
                    if e.floor.number==f.number and e.state!='moving':
                        f.dwb.on = False
                        if e.state!='opening' and e.state!='opened':
                            e.state = 'opening'
                    elevSet = True
                    break

    
            if not elevSet:
    
                # Nearest elevator above (moving down or stationary) = elev1
                for i in range(f.number+1, 10, 1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if e.direc=='down' or e.direc=='':
                                elev1 = e
                                elevSet = True
                                if e.state=='closed':
                                    break
                        if elev1!=None:
                            break

                # Nearest stationary elevator below
                for i in range(f.number-1, -1, -1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if e.direc=='':
                                elev2 = e
                                elevSet = True
                                break
                        if elevSet:
                            break

                dist1 = 10
                dist2 = 10

                # Compare which is closer
                if elev1!=None:
                    dist1 = abs(elev1.floor.number - f.number)
                if elev2!=None:
                    dist2 = abs(elev2.floor.number - f.number)

                # The elevator above is closer
                if dist1<=dist2 and elev1!=None:
                    elev1.dest.append(f.number)
                    elev1.direc = 'down'

                # The elevator below is closer
                elif dist2<dist1 and elev2!=None:
                    elev2.dest.append(f.number)
                    elev2.direc = 'up'

                # No optimal elevators found
                if elev1==None and elev2==None:
                    mindist = 10
                    for i in range(0, 10, 1):
                        if len(floors[i].elevs)>0:
                            e = floors[i].elevs[0]
                            if abs(e.floor.number-f.number) < mindist:
                                mindist = abs(e.floor.number-f.number)
                                elev1 = e
                    # elev1 is now the most available elevator somehow
                    elev1.dest.append(f.number)
                    if elev1.direc=='' and elev1.state!='closed' and elev1.state!='closing':
                        elev1.state = 'closing'




    for e in elevators:
        e.update(app.w, SH, floors)
    for f in floors:
        f.display.update(app.w)
    if simstate:
        master.after(5, simulate)


class App:
    def __init__(self, master):
        self.w = Canvas(master, width=SW/2-50, height=SH)
        self.m = Canvas(master, width=50, height=SH)
        self.f = Canvas(master, width=SW/2-100, height=SH)
        self.w.bind("<Button-1>", self.callelev)
        self.w.pack(side=LEFT)
        self.m.pack(side=TOP)
        self.f.pack(side=LEFT)
        
        self.makefloors()
        self.makelevs()
        
        self.start = Button(self.m, text="Start Simulation", command=self.sim)
        self.start.pack(side=LEFT)
        self.stop = Button(self.m, text="Stop Simulation", command=self.stop, state=DISABLED)
        self.stop.pack(side=LEFT)
        self.makepanels()

        self.f.bind("<Button-1>", self.operateelev)
        

    def operateelev(self, event):
        if not simstate:
            return
        x, y = event.x, event.y
        print 'clicked at [', x, y, ']'
        # if x>=100 and x<=250 and y>=50 and y<=250:
        #     # panel 1
        # elif x>=350 and x<=500 and y>=50 and y<=250:
        #     # panel 2
        # elif x>=100 and x<=250 and y>=350 and y<=550:
        #     # panel 3
        # elif x>=350 and x<=500 and y>=350 and y<=550:
        #     # panel 4


    def callelev(self, event):
        if not simstate:
            return
        x, y = event.x, event.y
        if x>=520 and x<=540:
            for i in range(10):
                if y>=30+i*SH/12 and y<=15+(2*i+1)*SH/24 and i>0:
                    floors[9-i].upb.on = True
                    break
                elif y>=25+(2*i+1)*SH/24 and y<=10+(i+1)*SH/12 and i<9:
                    floors[9-i].dwb.on = True
                    break

    def makefloors(self):
        global SW, SH, floordisplays, optelevdisplays
        self.w.create_text(300, 10, text='Halt time: '+str(opentime)+' milliseconds', font="Purisa 12 bold")
        for i in range(10):
            self.w.create_rectangle(105, 20+i*SH/12, 195, 20+(i+1)*SH/12, fill="#ccc")
            self.w.create_rectangle(205, 20+i*SH/12, 295, 20+(i+1)*SH/12, fill="#ccc")
            self.w.create_rectangle(305, 20+i*SH/12, 395, 20+(i+1)*SH/12, fill="#ccc")
            self.w.create_rectangle(405, 20+i*SH/12, 495, 20+(i+1)*SH/12, fill="#ccc")
            f = Floor(self.w, i, SH)
            if i<9:
                f.upb.floor = f
            if i>0:
                f.dwb.floor = f
            floors.append(f)
            
    def makepanels(self):
        global panels
        for i in range(4):
            p = Panel(self.f, i+1)
            panels.append(p)

    def makelevs(self):
        global SW, SH, elevators, floors
        for i in range(4):
            e = Elevator(self.w, i+1, SW, SH, floors[0])
            elevators.append(e)
            floors[0].elevs.append(e)

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

Label(master, text="Elevator Simulation",font="Purisa 18 bold underline").pack()
app = App(master)

master.mainloop()