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
                    elevSet = True

    
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
        for i in range(10):
            if i in e.dest:
                app.f.itemconfig(panels[e.number-1].b[i], fill='#6f9')
            else:
                app.f.itemconfig(panels[e.number-1].b[i], fill='#9bc')


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
        eidx = -1
        if x>=100 and x<=250 and y>=50 and y<=250:
            # panel 1
            eidx = 0
            x-=100
            y-=50
        elif x>=350 and x<=500 and y>=50 and y<=250:
            # panel 2
            eidx = 1
            x-=350
            y-=50
        elif x>=100 and x<=250 and y>=350 and y<=550:
            # panel 3
            eidx = 2
            x-=100
            y-=350
        elif x>=350 and x<=500 and y>=350 and y<=550:
            # panel 4
            eidx = 3
            x-=350
            y-=350

        if eidx!=-1 and x>=0 and y>=0:
            b = -1
            if x<50:
                # 1, 4, 7, open
                if y<40:
                    b = 7
                elif y<80:
                    b = 4
                elif y<120:
                    b = 1
                elif y<160:
                    b = 10

            elif x<100:
                # 0, 2, 5, 8, EM
                if y<40:
                    b = 8
                elif y<80:
                    b = 5
                elif y<120:
                    b = 2
                elif y<160:
                    b = 0
                elif y<200:
                    b = 12
            elif x<150:
                # 3, 6, 9, close
                if y<40:
                    b = 9
                elif y<80:
                    b = 6
                elif y<120:
                    b = 3
                elif y<160:
                    b = 11

            if b!=-1:
                # print eidx, b
                if b<10 and b not in elevators[eidx].dest and elevators[eidx].floor.number!=b:
                    elevators[eidx].dest.append(b)
                elif b==10 and elevators[eidx].state!='moving':
                    elevators[eidx].state = 'opening'
                elif b==11 and elevators[eidx].state=='opening' or elevators[eidx].state=='opened':
                    elevators[eidx].state = 'closing'

                # # Emergency
                # elif b==12:
                #     if elevators[eidx].state=='moving':
                #         self.dest = self.dest[0:1]
                #     else:
                #         elevators[eidx].dest = []
                #         if elevators[eidx].state!='opened' or elevators[eidx].state!='opening':
                #             elevators[eidx].state = 'opening'


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