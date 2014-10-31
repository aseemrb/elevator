#!/usr/bin/env python
# -*- coding: utf-8 -*-#

speed = 1
opentime = 3000
class Elevator(object):

    def __init__(self, w, number, SW, SH, floor, direc=''):
        self.number = number
        self.opendistance = 0.5
        self.direc = direc
        self.dest = []
        self.vel = 0
        self.floor = floor
        self.people = 0
        self.capacity = 6000
        self.timer = 0

        # state: moving, closed, opening, opened, closing
        self.state = 'closed'
        color = '#000000'
        self.body = w.create_rectangle(100*self.number+2, 20+(9-self.floor.number)*SH/12, 
            100*(self.number+1)-2, 20+(10-self.floor.number)*SH/12, 
            fill="#333")
        self.doorway = w.create_rectangle(100*self.number+50, 20+(9-self.floor.number)*SH/12, 
            100*self.number+50, 20+(10-self.floor.number)*SH/12, 
            fill="#fff")

        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        # self.label = w.create_text(self.x, self.y-10, text='Elevator'+str(self.number))

    def update(self, w, SH, floors):
        """ Called each frame. """
        if self.vel!=0:
            for i in range(10):

                # Reached some floor
                if self.y==20+(9-i)*SH/12:
                    self.floor.elevs.remove(self)
                    w.itemconfig(self.floor.display.body, fill='#6af')
                    if len(self.floor.elevs)==0:
                        w.itemconfig(self.floor.display.bodytext, text='--')
                    self.floor = floors[i]
                    floors[i].elevs.append(self)
                    w.itemconfig(self.floor.display.body, fill='#6fa')

                    # Update text on destination floors
                    for idx in self.dest:
                        if i==0 and self.direc=='up':
                            w.itemconfig(floors[idx].display.bodytext, text='G ↑')
                        elif i>0 and self.direc=='up':
                            w.itemconfig(floors[idx].display.bodytext, text=str(i)+' ↑')
                        elif self.direc=='down':
                            w.itemconfig(floors[idx].display.bodytext, text=str(i)+' ↓')

                    # Reached destination
                    if i in self.dest:
                        self.vel=0
                        # Remove from destination queue and open doors
                        self.dest.remove(i)
                        if i==0:
                            w.itemconfig(floors[i].display.bodytext, text='G')
                        else:
                            w.itemconfig(floors[i].display.bodytext, text=str(i))
                        self.state = 'opening'

                    break


        # Door opening animation
        if self.state=='opening':
            if self.floor.number<9:
                self.floor.upb.on = False
            if self.floor.number>0:
                self.floor.dwb.on = False

            # Do something for the timer here

            coordslist = w.coords(self.doorway)
            w.coords(self.doorway, coordslist[0]-self.opendistance,
                coordslist[1], coordslist[2]+self.opendistance, 
                coordslist[3])

        # Move elevator if state is moving
        elif self.state=='moving':
            w.move(self.body, 0, self.vel)
            w.move(self.doorway, 0, self.vel)

        # Door closing animation
        elif self.state=='closing':
            coordslist = w.coords(self.doorway)
            w.coords(self.doorway, coordslist[0]+self.opendistance,
                coordslist[1], coordslist[2]-self.opendistance, 
                coordslist[3])

        # Door opened
        if w.coords(self.doorway)[0]<=100*self.number+5:
            self.state = 'opened'
            self.timer += 10
            if self.timer>=opentime:
                self.state = 'closing'
                self.timer = 0
            if len(self.dest)==0:
                self.direc = ''
        
        # Door closed
        if w.coords(self.doorway)[0]>=100*self.number+50:
            self.state = 'closed'

            if len(self.dest)>0:
                if self.dest[0]>self.floor.number:
                    self.direc = 'up'
                    self.vel = -speed
                    self.state = 'moving'
                elif self.dest[0]<self.floor.number:
                    self.direc = 'down'
                    self.vel = speed
                    self.state = 'moving'

        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        w.update()
