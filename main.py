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
def simulate():
    global SH, elevators, floors, speed, panels
    for f in floors:
        if f.number<9:
            f.upb.update(app.w, SH)
        if f.number>0:
            f.dwb.update(app.w, SH)
        elev1 = None
        elev2 = None
        elevd = None
        minelevd = 10
        
        """Up button found on"""
        if (f.number<9 and f.upb.on) or (f.number==9 and f.dwb.on):
            elevSet = False
            # Elevator standing on the current floor
            for e in elevators:
                if e.people<e.capacity:
                    if (f.number in e.dest) or e.floor.number==f.number:
                        if e.floor.number==f.number and e.state!='moving':
                            f.upb.on = False
                            if e.state!='opening' and e.state!='opened':
                                e.state = 'opening'
                            elevSet = True
                            break
                        if abs(e.floor.number - f.number)<minelevd:
                            elevd = e
                            minelevd = abs(e.floor.number - f.number)

            if not elevSet:
                # # If already an ideal elevator is coming
                # for e in elevators:
                #     if len(e.dest)==1 and e.dest[0]==f.number:
                #         elevSet = True
                #         if e.state=='closed':
                #             break
                # if elevSet:
                #     break
                # # Finding the elevator that will reach the fastest
                # elevf1 = None
                # elevf2 = None
                # for i in range(f.number-1, -1, -1):
                #     if len(floors[i].elevs)>0:
                #         elevSet = False
                #         for e in floors[i].elevs:
                #             if (e.people<e.capacity) and len(e.dest)==0:
                #                 elevf1 = e
                #                 elevSet = True
                #                 if e.state=='closed':
                #                     break
                #         if elevf1!=None:
                #             break
                # for i in range(f.number+1, 10, 1):
                #     if len(floors[i].elevs)>0:
                #         elevSet = False
                #         for e in floors[i].elevs:
                #             if (e.people<e.capacity) and len(e.dest)==0:
                #                 elev2 = e
                #                 elevSet = True
                #                 if e.state=='closed':
                #                     break
                #         if elevf2!=None:
                #             break
                # dist1 = 10
                # dist2 = 10
                # if elevf1!=None:
                #     dist1 = f.number-elevf1.floor.number
                # if elevf2!=None:
                #     dist1 = elevf2.floor.number-f.number
                # if elevf1!=None and dist1<=dist2:
                #     elevf1.dest.append(f.number)
                #     elevf1.direc = 'up'
                #     continue
                # elif elevf2!=None and dist2<=dist1:
                #     elevf2.dest.append(f.number)
                #     elevf2.direc = 'down'
                #     continue

                # Nearest elevator below (moving up or stationary) = elev1
                for i in range(f.number-1, -1, -1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if (e.people<e.capacity) and (e.direc=='up' or e.direc==''):
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
                            if (e.people<e.capacity) and e.direc=='':
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

                if minelevd>dist1 or minelevd>dist2:
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
            elevd = None
            for e in elevators:
                if ((f.number in e.dest) or e.floor.number==f.number) and (e.people<e.capacity):
                    if e.floor.number==f.number and e.state!='moving':
                        f.dwb.on = False
                        if e.state!='opening' and e.state!='opened':
                            e.state = 'opening'
                        elevSet = True
                        break
                    if abs(e.floor.number - f.number)<minelevd:
                        elevd = e
                        minelevd = abs(e.floor.number - f.number)

    
            if not elevSet:    
                # Nearest elevator above (moving down or stationary) = elev1
                for i in range(f.number+1, 10, 1):
                    if len(floors[i].elevs)>0:
                        elevSet = False
                        for e in floors[i].elevs:
                            if (e.people<e.capacity) and (e.direc=='down' or e.direc==''):
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
                            if e.direc=='' and (e.people<e.capacity):
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

                if minelevd>dist1 or minelevd>dist2:
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
                app.f.itemconfig(panels[e.number-1].b[i], fill='#0f9')
            else:
                app.f.itemconfig(panels[e.number-1].b[i], fill='#9bc')

    for f in floors:
        f.display.update(app.w)

    for p in panels:
        if p.elev.direc=='up':
            if p.elev.floor.number==0:
                app.f.itemconfig(p.infolabel, text='G ↑')
            else:
                app.f.itemconfig(p.infolabel, text=str(p.elev.floor.number)+' ↑')
        if p.elev.direc=='down':
            if p.elev.floor.number==0:
                app.f.itemconfig(p.infolabel, text='G ↓')
            else:
                app.f.itemconfig(p.infolabel, text=str(p.elev.floor.number)+' ↓')
        if p.elev.direc=='':
            if p.elev.floor.number==0:
                app.f.itemconfig(p.infolabel, text='G')
            else:
                app.f.itemconfig(p.infolabel, text=str(p.elev.floor.number))
        
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
        self.f.create_text(50, 610, text='Status Key:')
        self.f.create_rectangle(110, 600, 130, 620, fill='#4c5')
        self.f.create_text(160, 610, text='Stable')
        self.f.create_rectangle(210, 600, 230, 620, fill='#47c')
        self.f.create_text(250, 610, text='Full')
        self.f.create_rectangle(290, 600, 310, 620, fill='#c54')
        self.f.create_text(340, 610, text='Overload')
        
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
                elif y<200:
                    b = 101 # pushin code

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
                elif y<200:
                    b = 102 # pushout code

            if b!=-1:
                if b<10 and b not in elevators[eidx].dest and elevators[eidx].floor.number!=b:
                    elevators[eidx].dest.append(b)
                elif b==10 and elevators[eidx].state!='moving':
                    elevators[eidx].state = 'opening'
                elif b==11 and (elevators[eidx].state=='opening' or elevators[eidx].state=='opened'):
                    elevators[eidx].state = 'closing'
                elif b==101 and elevators[eidx].state!='moving':
                    elevators[eidx].people += 1
                    self.f.itemconfig(panels[eidx].pcounter, text='People Inside: '+str(elevators[eidx].people))
                    if elevators[eidx].people == elevators[eidx].capacity:
                        self.f.itemconfig(panels[eidx].pcounterb, fill='#47c')
                    elif elevators[eidx].people > elevators[eidx].capacity:
                        self.f.itemconfig(panels[eidx].pcounterb, fill='#c54')
                    if elevators[eidx].state!='opened' and elevators[eidx].state!='opening':
                        elevators[eidx].state='opening'
                elif b==102 and elevators[eidx].state!='moving':
                    if elevators[eidx].state!='opened' and elevators[eidx].state!='opening':
                        elevators[eidx].state='opening'
                    elevators[eidx].people -= 1
                    if elevators[eidx].people<0:
                        elevators[eidx].people = 0
                    self.f.itemconfig(panels[eidx].pcounter, text='People Inside: '+str(elevators[eidx].people))
                    if elevators[eidx].people == elevators[eidx].capacity:
                        self.f.itemconfig(panels[eidx].pcounterb, fill='#47c')
                    elif elevators[eidx].people <= elevators[eidx].capacity:
                        self.f.itemconfig(panels[eidx].pcounterb, fill='#4c5')

                # Emergency
                elif b==12:
                    if elevators[eidx].state=='moving':
                        for i in elevators[eidx].dest[1:]:
                            self.w.itemconfig(floors[i].display.bodytext, text='--')
                        elevators[eidx].dest = elevators[eidx].dest[0:1]
                    else:
                        for i in elevators[eidx].dest:
                            self.w.itemconfig(floors[i].display.bodytext, text='--')
                        elevators[eidx].dest = []
                        if elevators[eidx].state!='opened' or elevators[eidx].state!='opening':
                            elevators[eidx].state = 'opening'

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
        global panels, elevators
        for i in range(4):
            p = Panel(self.f, i+1)
            p.elev = elevators[i]
            if p.elev.floor.number==0:
                p.infolabel = self.f.create_text(p.x+128, p.y-17, text='G')
            else:
                p.infolabel = self.f.create_text(p.x+128, p.y-17, text=str(p.elev.floor.number))
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